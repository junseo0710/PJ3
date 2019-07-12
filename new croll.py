import requests
from bs4 import BeautifulSoup
import urllib.request
req=requests.get('https://pokemon.fandom.com/ko/wiki/%EC%A0%84%EA%B5%AD%EB%8F%84%EA%B0%90')
html=req.text
soup=BeautifulSoup(html, 'html.parser')
imgurls=soup.select(
    'a > img '
)
data=[]
i=0
for url in imgurls:
    try:
        newurl = url.get('data-src')
        if i<3:
            i+=1
            continue
        else:

            a=newurl.split('"')
            data.append(a[0])
            i+=1
    except:
        pass
j=0
for j in range(len(data)):
    urllib.request.urlretrieve(data[j], "./img/" + str(j)+".png")
    j+=1


print(data)

