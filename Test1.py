>>> from bs4 import BeautifulSoup
>>> import requests
>>> import pandas as pd
>>> import re
>>> url="https://en.wikipedia.org/wiki/List_of_countries_by_GDP_(nominal)_per_capita"
>>> html_content = requests.get(url).text
>>> soup = BeautifulSoup(html_content, "lxml")
>>> gdp = soup.find_all("table", attrs={"class": "wikitable"})
>>> print("Number of tables on site: ",len(gdp))
('Number of tables on site: ', 3)
>>> print(soup)
