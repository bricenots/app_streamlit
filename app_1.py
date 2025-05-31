import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# -------------------------------
# Título e introducción
# -------------------------------
st.set_page_config(page_title="Visualizador de Datos - Streamlit")
st.title("📊 Visualizador Interactivo de Datos")
st.write("Sube un archivo `.csv`, selecciona las variables y visualiza distintos tipos de gráficos.")

# -------------------------------
# Subida de archivo
# -------------------------------
archivo = st.file_uploader("📁 Sube tu archivo CSV", type=["csv"])

if archivo is not None:
    # Leer el archivo CSV
    try:
        df = pd.read_csv(archivo)
        st.success("✅ Archivo cargado correctamente")
    except Exception as e:
        st.error(f"Error al leer el archivo: {e}")
        st.stop()

    # Mostrar preview del dataframe
    st.subheader("👀 Vista previa del archivo")
    st.dataframe(df.head())

    columnas = df.columns.tolist()

    # -------------------------------
    # Selección de variables
    # -------------------------------
    st.sidebar.header("⚙️ Configuración del gráfico")
    col_x = st.sidebar.selectbox("Variable X", columnas)
    col_y = st.sidebar.selectbox("Variable Y", columnas)

    tipo_grafico = st.sidebar.selectbox(
        "Tipo de gráfico",
        ["Línea", "Barras", "Dispersión", "Histograma", "Boxplot"]
    )

    # -------------------------------
    # Visualización
    # -------------------------------
    st.subheader(f"📈 Gráfico: {tipo_grafico} de {col_y} vs {col_x}")

    fig, ax = plt.subplots()
    try:
        if tipo_grafico == "Línea":
            ax.plot(df[col_x], df[col_y])
        elif tipo_grafico == "Barras":
            ax.bar(df[col_x], df[col_y])
        elif tipo_grafico == "Dispersión":
            ax.scatter(df[col_x], df[col_y])
        elif tipo_grafico == "Histograma":
            ax.hist(df[col_x].dropna(), bins=20, color='skyblue', edgecolor='black')
        elif tipo_grafico == "Boxplot":
            ax.boxplot(df[col_y].dropna())
            ax.set_xticks([1])
            ax.set_xticklabels([col_y])
        ax.set_xlabel(col_x)
        ax.set_ylabel(col_y)
        ax.grid(True)
        st.pyplot(fig)
    except Exception as e:
        st.error(f"Error al generar el gráfico: {e}")
