# -*- encoding:utf-8 -*-

from firstSpider.UrlManger import UrlManger
from firstSpider.HtmlDownloader import HtmlDownloader
from firstSpider.HtmlParser import HtmlParser
from firstSpider.DataOutput import DataOutput


class SpiderMan(object):
    def __init__(self):
        self.manger = UrlManger()
        self.downloader = HtmlDownloader()
        self.parser = HtmlParser()
        self.output = DataOutput()

    def spider(self, root_url):
        self.manger.add_new_url(root_url)
        while(self.manger.has_new_url() and self.manger.old_url_size() < 100):
            try:
                new_url = self.manger.get_new_url()
                html = self.downloader.download(new_url)
                new_urls, data = self.parser.parser(new_url, html)
                self.manger.add_new_urls(new_urls)
                self.output.store_data(data)
                print("已经抓取了%s个链接" % self.manger.old_url_size())
            except Exception:
                print("爬取失败")
        self.output.output_csv()


if __name__ == "__main__":
    url = "https://baike.baidu.com/item/%E7%BD%91%E7%BB%9C%E7%88%AC%E8%99%AB/5162711?fromtitle=%E8%9C%98%E8%9B%9B&fromid=8135707"
    spider_man = SpiderMan()
    spider_man.spider(url)
