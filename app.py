from sys import argv
from datetime import datetime
import requests

API_KEY = '8642ccb791a745e6ad534e0afd24da55'
URL = 'https://newsapi.org/v2/top-headlines?'

def get_articles_by_category(category=None, country='br'):
  
  query_parameters = {
    "category": category,
    "sortBy": "top",
    "country": country,
    "apiKey": API_KEY
  }

  response = requests.get(URL, params=query_parameters)
  print('Carregando suas notícias...\n')

  return parsing(response)

def parsing(response):
    articles = response.json()['articles']
        
    for article in articles:
        print('Título: ' + article["title"])
        print('Url: ' + article["url"])
        print('Publicado em: ' + convert_date(article["publishedAt"]))
        print('')

def convert_date(string):
  format_received = '%Y-%m-%dT%H:%M:%SZ' 
  format_to_show = '%d/%m/%Y às %H:%M'
  return datetime.strptime(string, format_received).strftime(format_to_show)

if __name__ == "__main__":
  try:
    if len(argv) > 1:
      category, contry = argv[1], argv[2]
      get_articles_by_category(category, contry)
    else:
      get_articles_by_category()
  except:
      print ('Uso: python app.py <categoria> <país> \nou apenas: python app.py')



  