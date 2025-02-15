import streamlit as st
import pandas as pd
import plotly.express as px  # type: ignore


@st.cache_data
def get_data(file) -> pd.DataFrame:
    df = pd.read_excel(file)
    return df


st.title("Display 2D Matrix from Excel")

# File upload
st.subheader("Upload an Excel file.")
uploaded_file = st.file_uploader("Excel File", type="xlsx")

# Convert to DataFrame
if uploaded_file:
    df = get_data(uploaded_file)
    st.write(uploaded_file.name)
    st.dataframe(df)

    # Select columns for visualization
    columns = df.columns.to_list()
    name = st.selectbox("Display Name", columns)
    color = st.selectbox("Color", columns)
    size = st.selectbox("Size", columns)
    x_columns = st.selectbox("X-Axis", columns)
    y_columns = st.selectbox("Y-Axis", columns)

    # Visualization
    if x_columns and y_columns:
        if x_columns == y_columns:
            st.error("X-Axis and Y-Axis cannot be the same.")
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
