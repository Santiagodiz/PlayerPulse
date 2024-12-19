# Interpretación exhaustiva de los resultados

## Descripción de las Métricas Utilizadas
Para la evaluación de nuestros resultados antes es relevante la comprensión de nuestras hipótesis:

    - La serie exógena de sentimiento acumulado (calculado mediante el sentimiento de las noticias del jugador X), afecta, en cualquier momento de la temporada, a la serie temporal del rendimiento de un jugador X. Donde X se trata de cualquiera de los jugadores planteados para este proyecto.

    - La serie exógena de sentimiento acumulado (calculado mediante el sentimiento de las noticias del jugador X), afecta, al final de temporada (con todos los datos de la temporada), a la serie temporal del rendimiento de un jugador X. Donde X se trata de cualquiera de los jugadores planteados para este proyecto.

Para probar esta hipótesis hemos obtenido dos tipos de resultados, mediante la comparación en la predicción de la serie, con y sin exógena (donde algún cambio en la predicción simboliza que la exógena afecta). Y, mediante la métrica de p-valor al realizar la predicción de la serie temporal usando la serie exógena. No nos hemos fijado en métricas como el AIC debido a nuestro objetivo de ajustar la predicción a los valores de rendimientos reales en vez de centrarnos en una predicción a futuro.

Para el primer resultado hemos hecho uso de métricas de error (media, desviación típica, mínimo, máximo, mediana), que calculan que tan bien se ajustan las predicciones a los rendimientos reales del jugador. Estas están calculadas mediante MSE.

Para el segundo resultado hemos comprobado la métrica del p-valor al predecir con la serie exógena los rendimientos, significando un menor valor, una mayor relevancia de la serie exógena sobre la predicción. Hemos tomado un umbral de 0.05 como un indicador de que la serie exógena afecta.

## Resultados de las Evaluaciones
Hemos realizado dos experimentos por jugador para evaluar tanto la predicción partido a partido, como la predicción de los últimos 30 días de la temporada. Para las predicciones partido a partido, entrenamos el modelo con los datos disponibles hasta el día previo al partido.

---

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


Por los resultados observados, en los que se aprecian ligeros cambios entre predicciones con y sin serie exógena, por jugador, hemos considerado que existe la posibilidad de que efectivamente la serie exógena afecte a la serie temporal de rendimiento. Aún así, para un análisis más confiable, hemos utilizado la métrica del p-valor, una métrica más estricta que nos dirá realmente si la serie exógena afecta.

---

Para el p-valor, no podemos mostrar exactamente los valores que hemos obtenido debido a la gran cantidad de ellos, ya que se calcula uno por cada predicción durante el experimento de partido a partido. Pero podemos explicar el desarrollo de este valor durante todas las predicciones realizadas.

En los experimentos de Ferrán Torres el p-valor, en la predición de final de temporada, es de 0, indicando una mayor relevancia de la serie exógena. Mientras que en las predicciones partido por partido, los p-valores comienzan cercanos a 1, y tienden a 0 al continuar en el tiempo, con alguna excepción donde en algún partido el p-valor sube a valores muy cercanos a 1, y en otras donde el p-valor es menor al umbral de 0.05. El p-valor acaba llegando a 0 al final de temporada.

El p-valor de Koundé en la predicción de fin de temporada es de un 0.61, lo que indica que no afecta la serie exógena. Para las predicciones partido a partido ocurre algo parecido con Ferrán, el p-valor disminuye pero ocurren ciertos partidos donde el p-valor es muy alto o más bajo, llegando solo un partido por debajo del umbral de 0.05. El valor final del p-valor es de 0.425.

Por último, el p-valor de Mikel Merino en la predicción de fin de temporada es de 0.006, por debajo del umbral, lo que muestra que impacta en la predicción. En las predicciones por partido el p-valor baja bastante rápido, manteniéndose por debajo del 0.6 y muchas veces bajando del umbral de 0.05. El p-valor acaba siendo de 0.063 en la última predicción.

## Limitaciones en la Evaluación
Una de la limitaciones es el tamaño de nuestra muestra. El número de noticias recopiladas durante la temporada 2023-2024 de LaLiga es reducido, lo que limita la capacidad de generalizar los hallazgos y detectar patrones estadísticamente significativos.

También existe un sesgo, al centrarse únicamente en una temporada, el análisis no captura variaciones a lo largo de varias temporadas que podrían ser importantes para validar la hipótesis.

Otra limitación es la de factores externos no controlados, aspectos como la vida privada, lesiones, accidentes u otros eventos externos que afectan al jugador y que no están reflejados en las métricas. Aunque podría haber correlación con las noticias, estos factores no son medidos directamente.

Otro posible sesgo es el de las noticias. Las métricas dependen de las noticias recopiladas. El sesgo inherente en la publicación de noticias (por ejemplo, preferencia hacia jugadores populares o eventos polémicos) podría afectar la representatividad de los datos.

En resumen, estas limitaciones destacan la necesidad de una muestra más amplia y considerar múltiples temporadas para mejorar la fiabilidad y alcance de los resultados.