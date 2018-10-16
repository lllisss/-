# -*- encoding:utf-8 -*-


class UrlManger(object):
    def __init__(self):
        self.new_urls = set()  # 未爬取url集合
        self.old_urls = set()  # 已爬取url集合

    def has_new_url(self):     # 判断是否有未爬取的url
        return self.new_url_size() != 0

    def get_new_url(self):  # 获取一个新的url
        new_url = self.new_urls.pop()
        self.old_urls.add(new_url)
        return new_url

    def add_new_url(self, url):
        if url is None:
            return
        if url not in self.new_urls and url not in self.old_urls:
            self.new_urls.add(url)

    def add_new_urls(self, urls):
        if urls is None and len(urls) == 0:
            return
        for url in urls:
            self.add_new_url(url)

    def new_url_size(self):  # 未爬取的url的大小
        return len(self.new_urls)

    def old_url_size(self):
        return len(self.old_urls)
