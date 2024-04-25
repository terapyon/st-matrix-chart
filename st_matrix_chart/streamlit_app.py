import streamlit as st
import pandas as pd
import plotly.express as px


if "uploaded_file" not in st.session_state:
    st.session_state.uploaded_file = None


@st.cache_data
def get_data(file) -> pd.DataFrame:
    df = pd.read_excel(file)
    return df


st.title("Excelから2次元マトリックスを表示")

# ファイルの読み込み
if st.session_state.uploaded_file is None:
    st.subheader("Excelファイルをアップロードします。")

    uploaded_file = st.file_uploader("Excelファイル", type="xlsx")
    if uploaded_file and st.button("アップロード"):
        st.session_state.uploaded_file = uploaded_file
        st.rerun()
else:
    st.subheader("アップロード済みのファイル")
    if st.button("ファイルを削除"):
        st.session_state.uploaded_file = None
        st.rerun()

    # DataFrame化
    df = get_data(st.session_state.uploaded_file)
    st.write(st.session_state.uploaded_file.name)
    st.dataframe(df)

    #  可視化に使うカラムを選択
    columns = df.columns.to_list()
    name = st.selectbox("表示名", columns)
    color = st.selectbox("色", columns)
    size = st.selectbox("円の大きさ", columns)
    x_columns = st.selectbox("横軸", columns)
    y_columns = st.selectbox("縦軸", columns)

    # 可視化
    if x_columns and y_columns:
        if x_columns == y_columns:
            st.error("横軸と縦軸が同じです。")
        else:
            fig = px.scatter(
                df,
                x=x_columns,
                y=y_columns,
                size=size,
                color=color,
                hover_name=name,
            )
            st.plotly_chart(fig)
