# Interpretación exhaustiva de los resultados

## Descripción de las Métricas Utilizadas
Para la evaluación de nuestros resultados antes es relevante la comprensión de nuestras hipótesis:

    - La serie exógena de sentimiento acumulado (calculado mediante el sentimiento de las noticias del jugador X), afecta, en cualquier momento de la temporada, a la serie temporal del rendimiento de un jugador X. Donde X se trata de cualquiera de los jugadores planteados para este proyecto.

    - La serie exógena de sentimiento acumulado (calculado mediante el sentimiento de las noticias del jugador X), afecta, al final de temporada (con todos los datos de la temporada), a la serie temporal del rendimiento de un jugador X. Donde X se trata de cualquiera de los jugadores planteados para este proyecto.

Para probar esta hipótesis hemos obtenido dos tipos de resultados, mediante la comparación en la predicción de la serie, con y sin exógena (donde algún cambio en la predicción simboliza que la exógena afecta). Y, mediante la métrica de p-valor al realizar la predicción de la serie temporal usando la serie exógena.

Para el primer resultado hemos hecho uso de métricas de error (media, desviación típica, mínimo, máximo, mediana), que calculan que tan bien se ajustan las predicciones a los rendimientos reales del jugador.

Para el segundo resultado hemos comprobado la métrica del p-valor al predecir con la serie exógena los rendimientos, significando un menor valor, una mayor relevancia de la serie exógena sobre la predicción. Hemos tomado un umbral de 0.05 como un indicador de que la serie exógena afecta.

## Resultados de las Evaluaciones
Hemos realizado dos experimentos por jugador para evaluar tanto la predicción partido a partido, como la predicción de los últimos 30 días de la temporada. Para las predicciones partido a partido, entrenamos el modelo con los datos disponibles hasta el día previo al partido.


Tabla de errores partido a partido:

| Errores día de partido               | Ferrán Torres (Con exógena) | Ferrán Torres (Sin exógena) | Koundé (Con exógena) | Koundé (Sin exógena) | Mikel Merino (Con exógena) | Mikel Merino (Sin exógena) |
|-------------------------|----------------------------|-----------------------------|-----------------------|----------------------|----------------------------|---------------------------|
| Mean error  | 1.888                    | 1.900                      | 1.629                | 1.635               | 1.884                      | 1.897                    |
| Std error  | 1.334                    | 1.329                      | 1.358                | 1.358               | 1.443                      | 1.453                    |
| Min error   | 0.023                    | 0.024                      | 0.044                | 0.047               | 0.035                      | 0.065                    |
| Max error   | 6.175                    | 6.169                      | 6.438                | 6.438               | 6.977                      | 6.984                    |
| Median error | 1.584                    | 1.596                      | 1.318                | 1.445               | 1.409                      | 1.420                    |



Tabla de errores al final de temporada:

| Errores día de partido                | Ferrán Torres (Con exógena) | Ferrán Torres (Sin exógena) | Koundé (Con exógena) | Koundé (Sin exógena) | Mikel Merino (Con exógena) | Mikel Merino (Sin exógena) |
|-------------------------|----------------------------|-----------------------------|-----------------------|----------------------|----------------------------|---------------------------|
| Mean error  | 1.408                     | 1.349                      | 1.227                | 1.328               | 1.927                      | 1.813                    |
| Std error  | 1.518                     | 1.048                      | 1.260                | 1.254               | 2.147                      | 1.441                    |
| Min error  | 0.221                     | 0.400                      | 0.009                | 0.079               | 0.063                      | 0.104                    |
| Max error  | 5.039                     | 3.755                      | 4.681                | 4.221               | 6.576                      | 5.195                    |
| Median error | 0.606                     | 1.197                      | 0.804                | 1.267               | 0.819                      | 1.551                    |

