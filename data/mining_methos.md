## 1. Descripción de las Técnicas Utilizadas

### a. Prueba de Estacionariedad (Dickey-Fuller)
Esta técnica se emplea para determinar si una serie temporal es **estacionaria**. La estacionariedad es un requisito importante para aplicar algunos modelos de predicción de series temporales, como ARIMA.
Método empleado: 
- Test de **Dickey-Fuller** (ADF).
Resultados esperados: Si el **p-valor** es menor a 0.05, se concluye que la serie es estacionaria.

### b. Análisis de Autocorrelación y Autocorrelación Parcial
Se utilizan gráficos de **Autocorrelación (ACF)** y **Autocorrelación Parcial (PACF)** para identificar y determinar el orden de los términos autoregresivos y de media móvil en modelos ARIMA.
Métodos empleados:
- ACF: Evalúa la correlación entre una observación y observaciones pasadas.
- PACF: Determina la relación entre una observación y una observación específica, eliminando otras influencias intermedias.

### c. Descomposición de Series Temporales
Descompone una serie temporal en tres componentes principales: **tendencia**, **estacionalidad** y **residuo**.
Método empleado: 
- Descomposición utilizando la función seasonal_decompose.
Resultados esperados: Identificar componentes, en especial estacionalidad, de la serie temporal para facilitar la modelización.

### d. Modelado de Tópics Dinámicos
Se utiliza LdaSeqModel para conseguir tanto los topics de las noticias como la evolución de estos a lo largo del tiempo. Este modelo analiza cómo cambian las distribuciones de palabras dentro de cada tópico en diferentes periodos temporales.
Técnicas utilizadas:
- Creación de un vocabulario a partir de las noticias.
- Filtrado de términos poco frecuentes o demasiado comunes para mejorar la calidad de los tópicos.
- División de los datos en periodos temporales basados en meses.


### e. Modelo SARIMAX
SARIMAX es una extensión del modelo ARIMA que incluye componentes estacionales y exógenos. Es utilizado para series temporales donde hay patrones cíclicos o estacionales. En este caso, se utiliza para predecir el rendimiento de los jugadores basado en las estadísticas históricas y tanto con otra serie exógena o no.
Características principales:
- Orden (p,d,q): Determina el modelo ARIMA base.
- Orden estacional (P,D,Q,s): Captura patrones cíclicos en intervalos definidos por s.
- Series exógenas: Variables adicionales que pueden influir en la predicción, en este caso se trata de el sentimiento positivo y negativo (acumulado o no) de noticias sobre cada uno de los jugadores.






## 2. Justificación de la Selección de Técnicas
### a. Prueba de Estacionariedad (ADF):
La estacionariedad es fundamental para aplicar modelos de predicción robustos como ARIMA. Verificar esta propiedad asegura que las predicciones sean consistentes.

### b. ACF y PACF:
Estas herramientas son esenciales para comprender la estructura de la serie temporal y definir correctamente los parámetros 𝑝 y 𝑞 para modelos de predicción.

### c. Descomposición de Series Temporales:
La descomposición facilita la identificación de patrones, lo que es útil tanto para la visualización como para obsevar estacionalidad.

### d. Modelado de Tópicos Dinámicos:
Permite capturar cómo evolucionan los temas relacionados con cada jugador y en general a lo largo de la temporada. Esto es esencial para identificar patrones o cambios significativos en las noticias vinculadas a los jugadores.

### e. Justificación de la Selección de SARIMAX
- Elegido para poder modelar tanto tendencias como estacionalidades en series temporales basadas en datos exógenos, ajustándose bien a los datos deportivos, donde el rendimiento de los jugadores puede seguir patrones cíclicos (por ejemplo, días de partido, competiciones regulares).
- Uso de series exógenas: Permite incluir variables adicionales (como el estado emocional derivado de noticias) que enriquecen el modelo y mejoran la precisión de las predicciones.
- Escenarios variados: El diseño flexible del código cubre distintas configuraciones:
1. Predicción de días específicos (como días de partido).
2. Predicción continua a partir de un punto definido en el tiempo.
3. Predicción a intervalos regulares.




## 3. Configuración de los Algoritmos
### a. Prueba de Estacionariedad (Dickey-Fuller)
Parámetros:
- Variable analizada: last_performance.
- Umbral de significancia: 0.05.
- Librerías utilizadas: statsmodels.tsa.stattools.adfuller.

### b. Análisis de ACF y PACF
Parámetros:
- Lags para ACF: 100.
- Lags para PACF: 30.
- Herramientas y librerías utilizadas: statsmodels.graphics.tsaplots.plot_acf y statsmodels.graphics.tsaplots.plot_pacf.

### c. Descomposición de Series Temporales
Parámetros:
- Modelo: additive.
- Periodo: Específico para los datos, configurado según las características de la serie temporal.
- Herramientas y librerías utilizadas: statsmodels.tsa.seasonal.seasonal_decompose.

### d. Preprocesamiento de Texto
Parámetros:
- Idioma de stopwords: inglés.
- Lematización: basada en WordNet.
- Longitud mínima de palabras: 3 caracteres.
- Herramientas y librerías utilizadas: nltk.corpus.stopwords, nltk.stem.WordNetLemmatizer, nltk.tokenize.word_tokenize

### e. Creación del Diccionario y Corpus
Parámetros:
- Términos mínimos en documentos (no_below): 5.
- Términos máximos en proporción (no_above): 0.5.
Librerías utilizadas: gensim.corpora.Dictionary para crear el vocabulario., gensim.models para transformar documentos al formato bag-of-words.

### f. Modelo de Tópicos Dinámicos (LdaSeqModel)
Parámetros:
- Número de tópicos (num_topics): 3.
- Varianza de la cadena temporal (chain_variance): 0.100.
- Iteraciones (passes): 10.
Librerías utilizadas: gensim.models.LdaSeqModel.

### g. modelo SARIMAX
Parámetros principales:
- order: (p, d, q). Definidos según pruebas preliminares en los datos históricos.
- seasonal_order: (P, D, Q, s). Ajustado para capturar estacionalidades.
Opciones de predicción:
- matches: Predice para días de partido.
- one: Predicción continua desde un punto inicial.
- step: Predicción a intervalos regulares definidos por step.
Series exógenas:
- exog: Datos adicionales relevantes (como sentimientos acumulados).
- no_future: Manejo de valores futuros para escenarios en los que esta información no está disponible.
