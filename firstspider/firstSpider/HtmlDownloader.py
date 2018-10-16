# -*- encoding:utf-8 -*-
import requests
class HtmlDownloader(object):
    def download(self,url):
        if url is None:
            return None
        header={
            "User-Agent":
            "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.3319.102 Safari/537.36"
        }
        html=requests.get(url,headers=header)
        if html.status_code==200:
            html.encoding="utf-8"
            return html.text
        return None