import os
from bs4 import BeautifulSoup

// Automation - WIP
printMsg1()

current_dir=r'C:/Apache24/htdocs/example'
for item in os.listdir(current_dir):
	if not os.path.isfile(item):
		for file in os.listdir(item):
			if file.endswith((".html", "_files")):
                	soup = BeautifulSoup(r.text, 'html.parser')
				Table = soup.find_all('table', attrs={'class':'table table-bordered'})
				print(Table)

printMsg2()
