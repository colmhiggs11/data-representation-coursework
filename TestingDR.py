from bs4 import BeautifulSoup
with open("Testing .html") as fp:
    soup1 = BeautifulSoup(fp, 'html.parser')
print(soup1.tr)
