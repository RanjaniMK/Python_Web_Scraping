#Python Script

import requests
r = requests.get('http://localhost/example/class-foafdocument.html')
from bs4 import BeautifulSoup
soup = BeautifulSoup(r.text, 'html.parser')
Table13= soup.find_all('table', attrs={'class':'table table-bordered'})
print(Table13)
