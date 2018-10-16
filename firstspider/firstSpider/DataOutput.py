# -*- encoding:utf-8 -*-
import csv


class DataOutput(object):
    def __init__(self):
        self.datas = []

    def store_data(self, data):
        if data is None:
            return
        self.datas.append(data)

    def output_csv(self):
        headers = ['链接','名称','摘要']
        with open('baike.csv', 'w',encoding='utf-8') as f:
            f_csv = csv.writer(f)
            f_csv.writerow(headers)
            f_csv.writerows(self.datas)
