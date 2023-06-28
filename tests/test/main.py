
# 特定の要素を抽出するコード
## import requests
## import bs4
## res = requests.get('https://tonari-it.com')
## res.raise_for_status()
## soup = bs4.BeautifulSoup(res.text, "html.parser")
## elems = soup.select('h2')
## for elem in elems:
##     print(elem)
##

# 特定の要素を抽出するコード
import requests
import bs4
URL = "https://kanazawa.ha4go.net/projects"
res = requests.get(URL)
res.raise_for_status()
# print(res.text)
soup = bs4.BeautifulSoup(res.text, "html.parser")
# soup = bs4.BeautifulSoup(res.text, "lxml")
# elems = soup.select(".all")
elems = soup.select(".content_title")
for elem in elems:
    print(elem)
