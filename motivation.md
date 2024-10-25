## Objetivo General del Proyecto
El objetivo de nuestro proyecto es comprobar si las noticias futbolísticas (tanto positivas como negativas), y la cantidad de estas, tienen algún tipo de efecto en el rendimiento de los futbolistas de los que hablan.

## Hipótesis
- **Impacto de los medios en el rendimiento de los jugadores:** EL número de noticias sobre un jugador que se publican en periodos entre partidos y dependiendo de si su contenido es positivo o negativo, influye directamente en el rendimiento de este en futuros partidos, en concreto en el más cercano, de la temporada 2023-2024 de LaLiga.
- **Efecto del rendimiento en el entorno mediático:** El efecto inverso. El rendimiento de cierto jugador en un partido tiene también un efecto directo en el tono y cantidad de noticias que se publicarán sobre ese jugador, durante la temporada 2023-2024 de LaLiga.

## Justificación de los Datos Seleccionados
Hemos recogido y preparado noticias publicadas durante la temporada 2023-2024 de LaLiga, de la misma forma también hemos preparado una fórmula para obtener el rendimiento de cada jugador por partido durante esta temporada. Con esto hemos creado un dataset unificado con las noticias publicadas sobre un jugador específico entre dos fechas (entre partidos), y su rendimiento en cada uno de estos partidos.Hemos considerado que el análisis de sentimiento de las noticias formará parte de una siguiente entrega.

Con esto deberíamos ser capaces de detectar patrones existentes entre el entorno mediático y su opinión sobre los jugadores y el rendimiento de estos durante la temporada 2023-2024 de LaLiga.

## Desafíos Potenciales con los Datos Limpiados
El **número total de noticias** que hemos sido capaces de recolectar no es muy grande. Además, como solo estamos analizando la temporada 2023-2024 de LaLiga, es posible que existan patrones que no podamos detectar en un periodo muy largo de tiempo, a lo largo de varias temporadas. Pero en este caso, hemos decidido acotar el análisis a una sola temporada para poder realizar un mejor análisis con el numero de noticias que hemos recolectado.

Además hay otros factores que no es posible tener en cuenta sobre los jugadores como su vida privada, accidentes/lesiones..., que pueden tener un efecto aún mayor sobre el rendimiento de esos jugadores. Aún así, se puede suponer que si un jugador es afectado por un factor externo a las noticias, es problable que este se vea reflejado en las noticias que se publican sobre el jugador.

En conclusión, nuestro proyecto esta acotado a una muestra de noticias pequeña e intentamos probar una hipótesis sobre un entorno afectado por infinidad de otros factores. Debido a estas razones, encontrar algo de significancia en los datos que hemos recolectado sería un gran logro, ya que implicaría que el entorno mediático tiene un efecto directo en el rendimiento de los jugadores de futbol y, en ese caso, hubieramos encontrado una manera plausible de predecir el rendimiento futuro próximo de un jugador en base a las noticias que se publican sobre el.