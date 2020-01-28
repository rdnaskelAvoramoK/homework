import requests
from bs4 import BeautifulSoup

url = 'https://minfin.com.ua/currency/nbu/'

source = requests.get(url)
main_text = source.text
soup = BeautifulSoup(main_text)

table = soup.find('table', {'class' : 'table-auto'})
tr = table.find('td', {'class' : 'responsive-hide'})
tr = tr.text

tr = tr[:5]

 print(tr)