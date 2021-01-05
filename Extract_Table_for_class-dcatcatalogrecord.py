#Python Script
import requests
r = requests.get('http://localhost/example/class-dcatcatalogrecord.html')
from bs4 import BeautifulSoup
soup = BeautifulSoup(r.text, 'html.parser')
Table2 = soup.find_all('table', attrs={'class':'table table-bordered'})
print(Table2)
