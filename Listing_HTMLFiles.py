#Lists all the .html files inside a folder
import os, glob
os.chdir("C:\Apache24\htdocs\example")
for file in glob.glob("*.html"):
        print(file)
