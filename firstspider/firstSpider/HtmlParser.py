# -*- encoding:"utf-8" -*-
from bs4 import BeautifulSoup
import re
import urllib.parse


class HtmlParser(object):

    def parser(self, page_url, page_html):
        if page_url is None or page_html == None:
            return
        soup = BeautifulSoup(page_html, "html.parser")
        new_urls = self._get_new_urls(page_url, soup)
        new_data = self._get_new_data(page_url, soup)
        return new_urls, new_data

    def _get_new_urls(self, page_url, soup):
        new_urls = set()
        links = soup.find_all('a', target="_blank")
        for link in links:
            new_url = link.get('href')
            new_full_url = urllib.parse.urljoin(page_url, new_url)
            new_urls.add(new_full_url)
        return new_urls

    def _get_new_data(self, page_url, soup):
        data = {}
        data['url'] = page_url
        title = soup.find("dd", class_="lemmaWgt-lemmaTitle-title").find('h1')
        data['title'] = title.get_text()
        summary = soup.find('div', class_="para")
        data['summary'] = summary.get_text()
        return data.values()
