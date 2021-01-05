#Python Script

import requests
r = requests.get('http://localhost/example/class-dcatresource.html')
from bs4 import BeautifulSoup
soup = BeautifulSoup(r.text, 'html.parser')
Table7 = soup.find_all('table', attrs={'class':'table table-bordered'})
print(Table7)
