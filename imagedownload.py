# -*- coding:UTF-8 -*-
import requests
from bs4 import BeautifulSoup
import re

header={'User-Agent': 'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.3319.102 Safari/537.36'}
for k in range(1,19):
    url="https://tieba.baidu.com/p/4452821383?pn="+str(k)
    res=requests.get(url,headers=header)
    photos=re.findall(r'<img class="BDE_Image" src="(.*?)"',res.text)
    for i in range(1,len(photos)):
        img = requests.get(photos[i])
        file_name=str(k)+str(i)+".jpg"
        with open(file_name, "wb") as f:
            f.write(img.content)
