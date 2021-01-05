#Python Script

import requests
r = requests.get('http://localhost/example/class-vcardkind.html')
from bs4 import BeautifulSoup
soup = BeautifulSoup(r.text, 'html.parser')
Table15= soup.find_all('table', attrs={'class':'table table-bordered'})
print(Table15)

