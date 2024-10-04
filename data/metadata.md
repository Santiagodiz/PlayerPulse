## General
Para formar el dataset, hemos recopilado por un lado las estadísticas individuales de diferentes jugadores de LaLiga en cada partido que disputaron durante la temporada 2023-24, 
y por otro distintas noticias y tweets sobre dichos jugadores en ese periodo de tiempo. La idea es analizar el impacto sobre su rendimiento que tienen los comentarios que reciben día a día.
Los objetivos que perseguimos con estos datos son los siguientes:
- **Afectación de las noticias y tweets en el rendimiento de los jugadores:** Queremos analizar si las noticias y tweets que se publican sobre los jugadores influyen en su rendimiento en los partidos.
- **Afectación del rendimiento de los jugadores en las noticias y tweets:** Por otro lado, queremos analizar si el rendimiento de los jugadores en los partidos influye en la cantidad y contenido de las noticias y tweets que se publican sobre ellos.

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

### Google News

- **Fuente de los datos:** Estas noticias son recolectadas de Google News, a través de un scrapeo web. Se han recopilado noticias sobre los jugadores de LaLiga en la temporada 2023-24.
- **Fecha de recogida:** 03/10/2024
- **Formato de los datos:** CSV compuestos por un resumen de la noticia, fecha de publicacion y un analisis de sentimiento.
- **Descripción de las variables o atributos:** El atributo principal es el analisis de sentimiento, que indica si la noticia es positiva, negativa. Además, necesitamos la fecha de publicación para poder colocar la noticia en el tiempo y ver si influye en el rendimiento del jugador en los partidos posteriores más cercanos.

### Fichajes.com

- **Fuente de los datos:** Noticias recolectadas de la página web de [fichajes.com](https://www.fichajes.com/actualidad), a través de web scraping. Noticias sobre fútbol del último año, octubre 2023-2024.
- **Fecha de recogida:** 29/09/2024
- **Formato de los datos:** CSV con las columnas de título, fecha de la noticia (día/mes), y contenido de la noticia.
- **Descripción de las variables o atributos:** El título y contenido de la noticia nos permitirán analizar el sentimiento de esta (positiva/negativa), mientras que la fecha nos permite colocar la noticia en el tiempo para conocer la relevancia de esta en el rendimiento del jugador del que se habla.
