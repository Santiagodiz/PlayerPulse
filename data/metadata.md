## General
Para formar el dataset, hemos recopilado por un lado las estadísticas individuales de diferentes jugadores de LaLiga en cada partido que disputaron durante la temporada 2023-24, 
y por otro distintas noticias y tweets sobre dichos jugadores en ese periodo de tiempo. La idea es analizar el impacto sobre su rendimiento que tienen los comentarios que reciben día a día.

## Estadísticas de los jugadores
- **Fuente de los datos:** Estos datos los hemos recolectado de la página web https://fbref.com/es, que ofrece un análisis estadístico detallado de cada uno de los partidos que se juegan
 durante las temporadas. Permite acceder al registro de partidos de cada jugador por temporada, proporcionando diferentes tablas con estadísticas diversas.
- **Fecha de recogida:** 03/10/2024
- **Formato de los datos:** CSVs con los datos de cada jugador.
- **Descripción de las variables o atributos:** Información sobre cada partido, como la fecha, equipos, competición o resultado, sobre la participación del jugador, como si fue titular,
minutos jugados o su posición, y estadísticas individuales variadas, tales como los goles, asistencias, regates, tarjetas, pases, acciones defensivas, remates, etc. En total son 118 variables.

Los datos se encuentran en el directorio */player_stats*.

## Tweets
- **Fuente de los datos:** Los datos se han obtenido de Twitter (X), pero dado que la API está limitada, ha sido a través de un scrapeo web a partir de Selenium. Recolecta tweets sobre una
búsqueda concreta entre las fechas proporcionadas.
- **Fecha de recogida:** 03/10/2024
- **Formato de los datos:** 
- **Descripción de las variables o atributos:**

## Noticias

- **Fuente de los datos:** 
- **Fecha de recogida:** 03/10/2024
- **Formato de los datos:** 
- **Descripción de las variables o atributos:** 
