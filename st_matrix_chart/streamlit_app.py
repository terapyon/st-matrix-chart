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
    temp_df = get_data(st.session_state.uploaded_file)
    ignored_columns = st.multiselect("無視する列", temp_df.columns.to_list())
    ignored_rows = st.multiselect("無視する行", temp_df.index.to_list())
    if ignored_rows:
        replace_columns = st.toggle("列名を置換する")
    else:
        replace_columns = False
    selected_df = temp_df.drop(ignored_rows, axis=0).drop(ignored_columns, axis=1)
    st.write(st.session_state.uploaded_file.name)

    if replace_columns:
        df = selected_df.iloc[1:, :]
        columns_name = selected_df.iloc[0, :]
        if columns_name.notna().all() and all(
            isinstance(name, str) for name in columns_name
        ):
            df.columns = columns_name
    else:
        df = selected_df

    st.dataframe(df)

    columns = df.columns.to_list()
    name = st.selectbox("表示名", columns)
    size = st.selectbox("円の大きさ", columns)
    color = st.selectbox("色", columns)
    x_columns = st.selectbox("横軸", columns)
    y_columns = st.selectbox("縦軸", columns)
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
