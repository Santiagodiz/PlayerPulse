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

| Errores                 | Ferrán Torres (Con exógena)  Ferrán Torres (Sin exógena) | Koundé (Con exógena)  Koundé (Sin exógena) | Mikel Merino (Con exógena)  Mikel Merino (Sin exógena) |
|-------------------------|------------------|-------------------|------------------|-------------------|------------------|-------------------|
|                         | Con exógena     | Sin exógena       | Con exógena     | Sin exógena       | Con exógena     | Sin exógena       |
| Mean error dia partido  | 1.8884540805832017 | 1.900071506583783 | 1.6286262353036407 | 1.6345071136519906 | 1.8840212790976212 | 1.8970185536569548 |
| Std error dia partido   | 1.3341601859495855 | 1.3288264941233718 | 1.3580577726994976 | 1.3583020537263915 | 1.4434120997648632 | 1.4534507743502514 |
| Min error dia partido   | 0.023176906486561677 | 0.024460002484102183 | 0.043508153954408435 | 0.04726345510186292 | 0.03522673316821656 | 0.0652342918349742 |
| Max error dia partido   | 6.175475901872003 | 6.16913299370233   | 6.438166311300639 | 6.438166311300577 | 6.976910928689424 | 6.9836092181943   |
| Median error dia partido| 1.5842122771180922 | 1.595903737428507  | 1.3184295251308784 | 1.445200477472004 | 1.408857338277143  | 1.4197644723378677 |


Tabla de errores al final de temporada:

| Errores                 | Ferrán Torres (Con exógena) | Ferrán Torres (Sin exógena)   | Koundé (Con exógena) |Koundé (Sin exógena) | Mikel Merino (Con exógena) | Mikel Merino (Sin exógena) |
|-------------------------|------------------|-------------------|------------------|-------------------|------------------|-------------------|
|                         | Con exógena     | Sin exógena       | Con exógena     | Sin exógena       | Con exógena     | Sin exógena       |
| Mean error dia partido  | 1.4082306018316777 | 1.3494335828536665 | 1.226667238968048 | 1.3281307669447873 | 1.9266847761755266 | 1.8128645251138613 |
| Std error dia partido   | 1.5178786145551812 | 1.0481283140910935 | 1.2597775451829767 | 1.2535706405934999 | 2.1466910168394095 | 1.4414016657653101 |
| Min error dia partido   | 0.22055186719274333 | 0.3997482899934517 | 0.009297530329475556 | 0.07926977398116986 | 0.06269663729819719 | 0.10406412761491168 |
| Max error dia partido   | 5.039047261180068 | 3.7547252647169373 | 4.681354572333654 | 4.220999742746211 | 6.576032163854023 | 5.1951626038306316 |
| Median error dia partido| 0.605865599931255  | 1.1967027018727605 | 0.8041617053458157 | 1.2665741276881737 | 0.8190219365219513 | 1.5509266370808032 |
