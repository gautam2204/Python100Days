import requests
from bs4 import BeautifulSoup, PageElement

resp=requests.get("https://www.tiaabank.com/")
#with open("tiaa.html","w") as file:
#    file.write(resp.text)

with open("tiaa.html") as file:
    html_doc = file.read()

soup=BeautifulSoup(markup=html_doc,features="html.parser")

print(soup.title.string)
for i in soup.find_all('a'):
    print(f"Type is {type(i)}")
    if isinstance(i,PageElement):
        print(i.get_text())
