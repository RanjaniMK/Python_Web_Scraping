>>> from bs4 import BeautifulSoup
>>> import requests
>>> import pandas as pd
>>> import re
>>> url="https://www.w3.org/TR/vocab-dcat-2/"
>>> html_content = requests.get(url).text
>>> soup = BeautifulSoup(html_content, "lxml")
>>> gdp = soup.find_all("table", id={"table-namespaces"})
>>> print("Number of tables on site: ",len(gdp))
('Number of tables on site: ', 1)
>>>print(soup)
