from bs4 import BeautifulSoup
import requests
import pandas as pd

# Creamos un DataFrame vacío
df = pd.DataFrame(columns=['title', 'date', 'content'])

# Iteramos sobre las páginas de noticias
for i in range(65, 377):
    url = f'https://www.fichajes.com/actualidad/{i}'
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    # Encuentra todos los articulos de la pagina
    news = soup.find_all('article')
    for new in news:
        # Recoge el metadata de cada articulo
        title = new.find('h3').text
        date = new.find('span').text

        # Entra en el articulo para recoger el contenido
        url = new.find('a')['href']
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')
        try:
            content1 = soup.find('h2', class_='articleLead').contents[0]
        except:
            content1 = ''
        try:
            content2 = ' '.join([p.text for p in soup.find('div', class_='wysiwygContent').find_all('p')])
        except:
            content2 = ''

        content = content1 + ' ' + content2
        df = pd.concat([df, pd.DataFrame({'title': [title], 'date': [date], 'content': [content]})])

    print(f'Page {i} scraped')

# Guardamos el DataFrame en un archivo CSV
df.to_csv('raw/fichajes_news.csv', index=False, sep=';')