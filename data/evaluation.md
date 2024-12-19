# Interpretación exhaustiva de los resultados

## Descripción de las Métricas Utilizadas
Para la evaluación de nuestros resultados antes es relevante la comprensión de nuestras hipótesis:

    - La serie exógena de sentimiento acumulado (calculado mediante el sentimiento de las noticias del jugador X), afecta, en cualquier momento de la temporada, a la serie temporal del rendimiento de un jugador X. Donde X se trata de cualquiera de los jugadores planteados para este proyecto.

    - La serie exógena de sentimiento acumulado (calculado mediante el sentimiento de las noticias del jugador X), afecta, al final de temporada (con todos los datos de la temporada), a la serie temporal del rendimiento de un jugador X. Donde X se trata de cualquiera de los jugadores planteados para este proyecto.

Para probar esta hipótesis hemos obtenido dos tipos de resultados, mediante la comparación en la predicción de la serie, con y sin exógena (donde algún cambio en la predicción simboliza que la exógena afecta). Y, mediante la métrica de p-valor al realizar la predicción de la serie temporal usando la serie exógena.

Para el primer resultado hemos hecho uso de métricas de error (medio, estándar, mínimo, máximo, mediano), que calculan que tan bien se ajustan las predicciones a los rendimientos reales del jugador.

Para el segundo resultado hemos comprobado la métrica del p-valor al predecir con la serie exógena los rendimientos, significando un menor valor, una mayor relevancia de la serie exógena sobre la predicción. Hemos tomado un umbral de 0.05 como un indicador de que la serie exógena afecta.

## Resultados de las Evaluaciones
Hemos realizado dos experimentos por jugador para evaluar tanto la predicción partido a partido, como la predicción de los últimos 30 días de la temporada.

- **Ferrán Torres**  

