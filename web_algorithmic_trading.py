from streamlit_option_menu import option_menu
import streamlit as st
import pandas as pd
import numpy as np
import pickle
from PIL import Image


st.set_page_config(
    page_title="Predicciones en el Trading Algoritmico utilizando Machine Learning",
    page_icon="https://cdn-icons-png.flaticon.com/512/8345/8345929.png",
    layout="wide",
    initial_sidebar_state="expanded"
)


# CSS para el fondo degradado
page_bg_css = """
<style>
[data-testid="stAppViewContainer"] {
    background: linear-gradient(180deg, #808080, #FFFFFF);  /* Plomo a blanco */
    background-size: cover;
}
</style>
"""
st.markdown(page_bg_css, unsafe_allow_html=True)

with st.sidebar:



    selected = option_menu(
        menu_title="Main Menu",
        options=["Home", "Diagnostic Measures", "Evaluate Data"],
        icons=["house", "droplet", "droplet-fill"],
        menu_icon="cast",
        styles={
            "container": {"padding": "5px", "background-color": "#f0f8ff"},  # Fondo del menú
            "nav-link": {
                "font-size": "16px",
                "text-align": "left",
                "margin": "0px",
                "--hover-color": "#87cefa",  # Azul claro al pasar el mouse
            },
            "nav-link-selected": {"background-color": "#4682b4", "color": "white"},  # Azul más oscuro para la selección
        },
    )

# Estilo CSS para los cuadros
box_style = """
<style>
.box {
  border: 1px solid black;
  padding: 10px;
  border-radius: 5px;
  background-color: #f9f9f9;
  margin-bottom: 20px;
  height: 400px; /* Altura fija */
  overflow-y: auto; /* Barra deslizadora */
  transition: transform 0.3s ease, box-shadow 0.3s ease; /* Transición suave */
}


.box:hover {
  transform: scale(1.07); /* Agranda el cuadro un 7% */
  box-shadow: 0px 8px 20px rgba(0, 0, 0, 0.3); /* Sombra más pronunciada */
}
</style>
"""


# Aplicar el estilo
st.markdown(box_style, unsafe_allow_html=True)

# Contenido del primer cuadro
content1 = """
<div class="box">
    <h4 style='text-align: center;'>Trading Algoritmico</h4>
    <p>Es el uso de programas informáticos para ejecutar operaciones financieras siguiendo reglas predefinidas basadas en precio, volumen, tiempo u otros factores. Los algoritmos analizan datos y ejecutan órdenes de manera eficiente, eliminando la intervención manual.</p>
    <img src="https://cdn.litemarkets.com/cache/uploads/blog_post/blog_posts/algorithmic-trading-in-forex/preview.jpg?q=75&w=1000&s=4f0f69e42dcf41ab10a1a065e932b4a6" alt="Imagen en el cuadro 1" width="100%">
</div>
"""

# Contenido del segundo cuadro
content2 = """
<div class="box">
    <h4 style='text-align: center;'>Machine Learning</h4>
    <p>Es un campo de la inteligencia artificial que permite a los sistemas aprender patrones a partir de datos y hacer predicciones o tomar decisiones sin ser explícitamente programados. En trading, ML se usa para identificar tendencias, predicciones de precios y gestión de riesgos.</p>
    <img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSF-KHSqTu4Yf42u0FPBQvR2pRO80CC_jQuvA&s" alt="Imagen en el cuadro 2" width="100%">
</div>
"""

# Contenido del tercer cuadro
content3 = """
<div class="box">
    <h4 style='text-align: center;'>Beneficios</h4>
    <p>Algunos beneficios del trading algorítmico utilizando machine learning incluyen un análisis avanzado de grandes volúmenes de datos históricos y en tiempo real, lo que permite identificar patrones complejos; mejoras en la precisión de las predicciones gracias a la capacidad de aprendizaje y adaptación de los modelos; ejecución rápida y eficiente de operaciones para aprovechar oportunidades en el mercado; reducción de sesgos humanos al tomar decisiones basadas en datos; optimización y ajuste dinámico de estrategias ante cambios en las condiciones del mercado; y automatización de estrategias complejas que serían inviables de gestionar manualmente.</p>
    <img src="https://dropinblog.net/34249715/files/1622-trading-algoritmico.jpg" alt="Imagen en el cuadro 3" width="100%">
</div>
"""

# Mostrar los cuadros en Streamlit
#st.markdown(content1, unsafe_allow_html=True)
#st.markdown(content2, unsafe_allow_html=True)
#st.markdown(content3, unsafe_allow_html=True)




if selected == "Home":


    #st.markdown("<h1 style='text-align: center;'><span style='color: #ff6347;'>🔥</span>Predecir donde invertir de acuerdo al diagnostico='color: #32cd32;'>🌱</span></h1>", unsafe_allow_html=True)
    st.markdown("""<h1 style="text-align: center;">Predicciones en el Trading Algoritmico utilizando el Machine Learning</h1>""", unsafe_allow_html=True)
    st.write("")
    st.write("")
 
    col1, col2, col3  = st.columns([1, 1, 1])
   

    # Columna 1: Texto

   # col1.markdown("""<h4 style="text-align: center;">Trafing Algoritmico</h4>""", unsafe_allow_html=True)
   # col1.write("Es el uso de programas informáticos para ejecutar operaciones financieras siguiendo reglas predefinidas basadas en precio, volumen, tiempo u otros factores. Los algoritmos analizan datos y ejecutan órdenes de manera eficiente, eliminando la intervención manual.")
    col1.markdown(content1, unsafe_allow_html=True)

    # Columna 2: Texto

    #col2.markdown("""<h4 style="text-align: center;">Machine Learning</h4>""", unsafe_allow_html=True)
    #col2.write("Es un campo de la inteligencia artificial que permite a los sistemas aprender patrones a partir de datos y hacer predicciones o tomar decisiones sin ser explícitamente programados. En trading, ML se usa para identificar tendencias, predicciones de precios y gestión de riesgos.")
    col2.markdown(content2, unsafe_allow_html=True)
    
    # Columna 3: Texto

    #col3.markdown("""<h4 style="text-align: center;">Benefits</h4>""", unsafe_allow_html=True)
    #col3.write("Algunos beneficios del trading algorítmico utilizando machine learning incluyen un análisis avanzado de grandes volúmenes de datos históricos y en tiempo real, lo que permite identificar patrones complejos; mejoras en la precisión de las predicciones gracias a la capacidad de aprendizaje y adaptación de los modelos; ejecución rápida y eficiente de operaciones para aprovechar oportunidades en el mercado; reducción de sesgos humanos al tomar decisiones basadas en datos; optimización y ajuste dinámico de estrategias ante cambios en las condiciones del mercado; y automatización de estrategias complejas que serían inviables de gestionar manualmente.")
    col3.markdown(content3, unsafe_allow_html=True)

 #col2.image("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQgH4h2OmskN2vK8ptBQAh3xg6m42clgnFZMg&s", width= 600)
    # Columna 2: Texto
    # 


    st.write("---")

            

 


    # Main title
    st.title("📈 Comprenciendo el Trading Algoritmico")

    # Creating two columns
    colA1, colA2 = st.columns([2,1])

    # Column 1: What is Asthma? and Symptoms
    with colA1:
        st.header("¿Que es el Trading Algoritmico?")
        st.write("""
        El trading algorítmico es el uso de programas informáticos para ejecutar operaciones financieras de manera automatizada. Estos programas siguen reglas predefinidas basadas en criterios como el precio, el volumen o el tiempo, y pueden analizar grandes cantidades de datos rápidamente para tomar decisiones de inversión sin intervención humana. Su objetivo es mejorar la eficiencia, reducir errores humanos y aprovechar oportunidades de mercado en tiempo real.
        """)

        
        #caption="Representation of asthma and airways"
        
        st.header("Componentes Claves en el Trading Algorítmico")
        st.markdown("""
        - Algoritmos de ejecución: Deciden cuándo, cómo y a qué precio ejecutar las órdenes.
        - Modelos de predicción: Utilizan técnicas como el análisis técnico, análisis fundamental o machine learning para predecir movimientos de mercado.
        - Infraestructura tecnológica: Necesaria para ejecutar algoritmos rápidamente, incluyendo servidores y conexiones directas con los mercados. 
        - Gestión del riesgo: Los algoritmos implementan estrategias para controlar el riesgo, como el uso de stops automáticos o estrategias de diversificación.
        """)

        st.header("Ramas del Trading Algoritmico")
        st.markdown("""
        - *Trading de Alta Frecuencia (HFT):*        
            Se basa en ejecutar un gran número de operaciones en fracciones de segundo. Este tipo de trading aprovecha pequeñas diferencias en los precios de los activos para obtener ganancias.  
                    
        - *Arbitraje:*       
            Consiste en aprovechar las discrepancias de precios entre diferentes mercados o activos. Por ejemplo, comprar un activo a un precio bajo en un mercado y venderlo a un precio más alto en otro. 
                    
        - *Market Making:*      
            Los market makers proporcionan liquidez en los mercados ofreciendo precios de compra y venta de activos. El algoritmo ajusta continuamente los precios en función de la oferta y la demanda, para ganar una pequeña comisión por transacción.  
                    
        - *Trend Following (Seguimiento de tendencias):*     
            Se basa en identificar y seguir tendencias de mercado. Los algoritmos ejecutan operaciones cuando detectan que un activo está en una tendencia alcista o bajista, buscando aprovechar esa tendencia. 
                    
        - *Statistical Arbitrage:*    
            Utiliza modelos estadísticos y matemáticos para encontrar oportunidades de arbitraje basadas en la correlación entre diferentes activos. Los algoritmos buscan patrones en los precios y ejecutan transacciones cuando estos patrones se rompen. 
                     
        """)
        st.header("Ventajas del Trading Algorítmico:")
        st.markdown("""
        *Eficiencia:*
        Los algoritmos pueden analizar grandes volúmenes de datos rápidamente y tomar decisiones en tiempo real.
                    
        *Reducción de errores humanos:* 
        Las decisiones se basan en datos y reglas predefinidas, eliminando los sesgos emocionales y errores humanos.
                    
        *Costos operativos reducidos:* 
        Menor necesidad de intervención humana, lo que reduce costos de gestión y operación.
                    
        *Ejecutar estrategias complejas:* 
        Los algoritmos pueden manejar estrategias sofisticadas que serían difíciles de ejecutar manualmente.
                    
        *Acceso a oportunidades de mercado:* 
        Capacidad para reaccionar rápidamente a cambios en los precios de activos y aprovechar oportunidades en mercados de alta frecuencia. 
                    
        """)

        st.header("Desventajas del Trading Algorítmico")
        st.markdown("""
        *Dependencia tecnológica:*
        Si el sistema falla o experimenta errores, puede resultar en grandes pérdidas.
                    
        *Costos iniciales elevados:*
        Requiere infraestructura avanzada y personal especializado.
                    
        *Riesgo de sobreoptimización:* 
        Si los modelos no se ajustan correctamente, pueden operar de manera incorrecta o fallar en condiciones del mercado no previstas.
                    
        """)
        

    # Column 2: Causes, Management, and When to Seek Help
    with colA2:
        st.write("---")
        st.image("https://fastercapital.com/es/i-es/Comercio-algoritmico--maximizar-las-ganancias-con-acceso-directo-al-mercado--Componentes-clave-de-un-sistema-de-comercio-algor-tmico.webp",use_container_width=True)
        st.write("")
        st.write("---")
        st.write("")
        st.image("https://img.freepik.com/fotos-premium/hombre-esta-pie-frente-grafico-que-dice-mano_1047061-7007.jpg",use_container_width=True)
        st.write("")
        st.write("---")
        st.write("")
        st.image("https://static.vecteezy.com/system/resources/previews/005/216/356/non_2x/coins-bar-with-arrow-graph-going-up-and-down-growth-of-financial-and-economy-business-infographic-vector.jpg",use_container_width=True)
        st.write("---")





    st.write("---")


    # Main title
    st.title("🧠 Machine Learning")

     # Creating two columns
    colM1, colM2 = st.columns([2,1])

    with colM1:

        # Section: What is Machine Learning?
        st.header("¿Que es el Machine Learning?")
        st.write("""
        El aprendizaje automático (ML) es un campo de la inteligencia artificial que permite a las máquinas aprender de los datos y mejorar su rendimiento en tareas específicas sin necesidad de ser programadas explícitamente. Utiliza algoritmos que identifican patrones y relaciones en los datos, generando modelos predictivos.
        """)

        # Illustrative image
        

        # Section: Types of Machine Learning
        st.header("Tipos de aprendizaje automático")
        st.markdown("""
        1. *Aprendizaje supervisado*  
        Los algoritmos aprenden a partir de datos etiquetados.
        *Ejemplo:* clasificar correos electrónicos como "spam" o "no spam". 
        

        2. *Aprendizaje no supervisado:*  
        Encuentra patrones en datos no etiquetados.
        *Ejemplo:* segmentación de clientes en marketing.

        3. *Reinforcement Learning:*  
        Basado en premios y castigos para aprender. 
        *Ejemplo:* robots jugando videojuegos.
        """)

        # Section: Key Benefits of Machine Learning
        st.header("Principales beneficios del aprendizaje automático")
        st.markdown("""
        1. *Precisión y predicciones mejoradas:* Identifica patrones complejos con alta precisión.  
        2. *Análisis rápido de datos:* Procesa grandes cantidades de datos en tiempo real.
        3. *Experiencias Personalizadas:*  Adapta los servicios a las necesidades de cada usuario.
        4. *Detección de fraudes* Identifica anomalías en las transacciones y previene el fraude.
        5. *Innovación de productos:* Facilita el desarrollo de nuevos servicios como vehículos autónomos.
        """)
    

    with colM2:

        st.image("https://miro.medium.com/v2/resize:fit:1080/1*YgXPZN3y0wJ6NnnfpaM1qA.png",use_container_width=True)
        st.write("---")
        st.image("https://www.mastermarketing-valencia.com/marketing-digital/wp-content/uploads/sites/1/2020/10/Infografia-beneficios-Machine-Learning-para-ecommerce.jpg",use_container_width=True)



if selected == "Diagnostic Measures":



    # Cargar el modelo entrenado
    with open("GradientBoosting.pkl", "rb") as file:
        model = pickle.load(file)

    # Función para recopilar la entrada del usuario
    def get_user_input():
        # Entradas para las características
        Time = st.slider("Tiempo del mercado(segs.)", 1495181760000, 1550471340000, 1605760920000)  # Reemplaza 'Time'
        OpenM = st.slider("Valor inicial del mercado.", 1611, 9268, 16925)  # Reemplaza 'OpenM'
        CloseM = st.slider("Valor final del mercado.", 1612, 9268, 16925)  # Reemplaza 'CloseM'
        HighM = st.slider("Valor más alto del mercado.", 1612, 9268, 16925)  # Reemplaza 'HighM'
        LowM = st.slider("Valor más bajo del mercado.", 1611, 9268, 16925)  # Reemplaza 'LowM'
        VolumeM = st.slider("Volumen del mercado.", 0, 577, 1154)  # Reemplaza 'VolumeM'
  

        # Crear un diccionario con las características
        user_data = {
            "time": Time,  # Time
            "open": OpenM,  # OpenM
            "close": CloseM,  # CloseM
            "high": HighM,  # HighM
            "low": LowM,  # LowM
            "volume": VolumeM,  # VolumeM

        }

        # Transformar los datos en un DataFrame
        features = pd.DataFrame(user_data, index=[0])
        return features

    # Título de la aplicación
    st.title("Predicción del Mercado del Trading Algorítmico")
    st.write("Ingrese las características del mercado para predecir si es probable que se eleve el precio del mercado.")

    # Recopilar entrada del usuario
    user_input = get_user_input()

    # Botón para hacer la predicción
    if st.button("Evaluar"):
        prediction = model.predict(user_input)
        probability = model.predict_proba(user_input)

        # Obtener la probabilidad más alta
        argmax = np.argmax(probability)
        probability = probability[0]

        # Mostrar resultados
        st.subheader("Resultado")
        classification_result = "El mercado se eleva." if prediction[0] == 1 else "El mercado disminuye."
        st.success(classification_result)

        st.subheader("Confianza del modelo")
        st.success(f"{(probability[argmax] * 100):.2f}%")


if selected == "Evaluate Data":


    # Cargar el modelo entrenado
    with open("GradientBoosting.pkl", "rb") as file:
        model = pickle.load(file)

    # Función para aplicar el estilo en los campos de entrada (incluyendo la barra de deslizamiento)
    def set_input_style():
        st.markdown("""
            <style>
            .stSlider .st-bd {
                background-color: #b3cde0;  /* Color azul claro para la barra de fondo */
            }
            .stSlider .st-au {
                background-color: #3a58a7;  /* Color azul más oscuro para el 'thumb' (el círculo) */
            }
            .stSlider .st-bw {
                background-color: #3a58a7;  /* Color azul más oscuro para la barra activa */
            }
            </style>
        """, unsafe_allow_html=True)

    # Título de la aplicación
    st.title("Predicción del Mercado del Trading Algorítmico")
    st.write("Ingrese las características del mercado para predecir si es probable que se eleve.")

    # Aplicar el estilo azul a los campos de entrada
    set_input_style()

    # Cargar archivo de datos para evaluar
    st.header('Evaluar datos cargados desde medidas diagnósticas')
    uploaded_file = st.file_uploader("Sube tu archivo:", type=["csv"])

    if uploaded_file:
        st.subheader('Datos de entrada')
        # Leer el archivo CSV cargado
        df = pd.read_csv(uploaded_file, float_precision="round_trip")

        # Extraer las columnas necesarias (ajustar el índice de columnas según corresponda)
        X = df[["time", "open", "close",
                "high", "low", "volume"]].values

        # Realizar predicciones
        prediction = model.predict(X)
        probability = model.predict_proba(X)
        argmax = np.argmax(probability, axis=1)

        # Crear una copia del DataFrame con las predicciones y probabilidades
        df2 = df[["time", "open", "close",
                "high", "low", "volume"]]

        # Asignar resultados de predicción (positivo o negativo para la subida del mercado)
        pred = ["El mercado subirá" if i == 1 else "El mercado no subirá" for i in prediction]

        # Asignar las probabilidades de cada clase (no asma y asma)
        no_mercado_accuracy = [f"{(i * 100).round(2)}%" for i in probability[:, 0]]
        mercado_accuracy = [f"{(i * 100).round(2)}%" for i in probability[:, 1]]

        # Agregar los resultados al DataFrame
        df2['Resultado'] = pred
        df2['Confianza en la no subida del mercado'] = no_mercado_accuracy
        df2['Confianza en la subida del mercado'] = mercado_accuracy

        # Mostrar el DataFrame con los resultados
        st.write(df2)
