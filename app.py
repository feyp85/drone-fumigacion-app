
import streamlit as st
import pandas as pd

# Datos base de parámetros por cultivo
cultivos_data = {
    "Banano": {"tasa_aplicacion": 18, "velocidad": "20-30 km/h", "altura": "7-8 m", "ancho_faja": "7-9.5 m", "gota": "Fina/Media"},
    "Maíz": {"tasa_aplicacion": 19, "velocidad": "20-25 km/h", "altura": "5-6 m", "ancho_faja": "7-8.5 m", "gota": "Fina/Media/Gruesa"},
    "Arroz": {"tasa_aplicacion": 16.5, "velocidad": "25-30 km/h", "altura": "4-7 m", "ancho_faja": "6.5-8 m", "gota": "Muy Fina/Fina/Media"},
    "Cacao": {"tasa_aplicacion": 25, "velocidad": "20-25 km/h", "altura": "7 m", "ancho_faja": "7-8.5 m", "gota": "Muy Fina/Fina/Media"},
}

# Configuración de la app
st.title("Aplicativo de Fumigación con Dron DJI Agras T50")
st.write("Ingrese los parámetros para obtener las recomendaciones técnicas.")

# Entradas del usuario
cultivo = st.selectbox("Seleccione el cultivo", list(cultivos_data.keys()))
hectareas = st.number_input("Ingrese la cantidad de hectáreas", min_value=0.1, step=0.1)
dilucion = st.number_input("Ingrese el porcentaje de dilución del producto (%)", min_value=0.0, step=0.1)

# Lógica de cálculo
if cultivo and hectareas:
    datos = cultivos_data[cultivo]
    tasa = datos["tasa_aplicacion"]
    total_solucion = tasa * hectareas
    producto_puro = total_solucion * (dilucion / 100)
    vuelos = total_solucion / 40  # tanque del T50
    tiempo_estimado = vuelos * 10 / 60  # 10 min por vuelo, convertido a horas

    # Resultados
    st.subheader("Recomendaciones Técnicas")
    st.write(f"**Velocidad de vuelo:** {datos['velocidad']}")
    st.write(f"**Altura de vuelo:** {datos['altura']}")
    st.write(f"**Ancho de faja recomendado:** {datos['ancho_faja']}")
    st.write(f"**Tamaño de gota:** {datos['gota']}")
    st.write(f"**Tasa de aplicación:** {tasa} L/ha")

    st.subheader("Cálculos Operativos")
    st.write(f"**Solución total a aplicar:** {total_solucion:.2f} litros")
    st.write(f"**Producto puro necesario:** {producto_puro:.2f} litros")
    st.write(f"**Número de vuelos requeridos:** {vuelos:.0f} vuelos")
    st.write(f"**Tiempo estimado de operación:** {tiempo_estimado:.2f} horas")
