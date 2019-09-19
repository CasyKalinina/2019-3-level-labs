import requests
from bs4 import BeautifulSoup

page_url = 'https://lenta.ru/rubrics/culture/'

lenta_culture_request = requests.get(page_url)

lenta_culture_content=lenta_culture_request.text

if lenta_culture_request.status_code == 200:
  print('Success!')
else:
  print('Error!')
  
parsed_page = BeautifulSoup(lenta_culture_content)
 
print(type(parsed_page))

print(parsed_page.title)
