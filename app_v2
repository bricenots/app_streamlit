import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="Visualizador de Datos - Streamlit")
st.title("📊 Visualizador Interactivo de Datos")
st.write("Sube un archivo `.csv`, selecciona las variables y visualiza distintos tipos de gráficos.")

# Subida de archivo
archivo = st.file_uploader("📁 Sube tu archivo CSV", type=["csv"])

if archivo is not None:
    try:
        df = pd.read_csv(archivo)
        st.success("✅ Archivo cargado correctamente")
    except Exception as e:
        st.error(f"Error al leer el archivo: {e}")
        st.stop()

    st.subheader("👀 Vista previa del archivo")
    st.dataframe(df.head())

    columnas = df.columns.tolist()

    # Configuración desde barra lateral
    st.sidebar.header("⚙️ Configuración del gráfico")
    tipo_grafico = st.sidebar.selectbox(
        "Tipo de gráfico",
        ["Línea", "Barras", "Dispersión", "Histograma", "Boxplot"]
    )

    if tipo_grafico in ["Histograma", "Boxplot"]:
        col = st.sidebar.selectbox("Variable", columnas)
    else:
        col_x = st.sidebar.selectbox("Variable X", columnas)
        col_y = st.sidebar.selectbox("Variable Y", columnas)

    st.subheader(f"📈 Gráfico: {tipo_grafico}")

    fig, ax = plt.subplots()
    try:
        if tipo_grafico == "Línea":
            ax.plot(df[col_x], df[col_y])
        elif tipo_grafico == "Barras":
            ax.bar(df[col_x], df[col_y])
        elif tipo_grafico == "Dispersión":
            ax.scatter(df[col_x], df[col_y])
        elif tipo_grafico == "Histograma":
            ax.hist(df[col].dropna(), bins=20, color='skyblue', edgecolor='black')
            ax.set_xlabel(col)
        elif tipo_grafico == "Boxplot":
            ax.boxplot(df[col].dropna())
            ax.set_xticks([1])
            ax.set_xticklabels([col])
            ax.set_ylabel(col)
        ax.grid(True)
        st.pyplot(fig)
    except Exception as e:
        st.error(f"Error al generar el gráfico: {e}")
