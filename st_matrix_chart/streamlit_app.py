import streamlit as st
import pandas as pd
import plotly.express as px


@st.cache_data
def get_data(file) -> pd.DataFrame:
    df = pd.read_excel(file)
    return df


st.title("Excelから2次元マトリックスを表示")

# ファイルの読み込み
st.subheader("Excelファイルをアップロードします。")
uploaded_file = st.file_uploader("Excelファイル", type="xlsx")

# DataFrame化
if uploaded_file:
    df = get_data(uploaded_file)
    st.write(uploaded_file.name)
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
