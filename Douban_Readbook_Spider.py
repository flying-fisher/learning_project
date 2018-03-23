# -*- coding:utf-8 -*-
import requests
from lxml import etree
import json

class Douban_Readbook_Spider():

    def __init__(self):
        self.url_tem = 'https://read.douban.com/kind/1?start={}&sort=new&promotion_only=False&min_price=None&max_price=None&works_type=None'
        self.headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36"}

    def get_url_list(self):
        url_lists = [self.url_tem.format(str(i)) for i in range(0,2000,20)]
        return url_lists

    def parse_url_list(self,url):
        response = requests.get(url,headers = self.headers)
        return response.content.decode()

    def get_content_url(self,html_content):
        content = etree.HTML(html_content)
        # 分组
        div_list = content.xpath("//ul[@class='list-lined ebook-list column-list']/li[@class='item store-item']")
        #print(div_list)
        book_list = []

        for div in div_list:
            item = {}
            item["books_name"] = div.xpath(".//div[@class='title']/a/text()")
            item["books_url"] = "https://read.douban.com"+ div.xpath(".//div[@class='title']/a/@href")[0]
            item["books_author"] = div.xpath(".//div[@class='info']/p//span[@class='labeled-text']/a/text()") #+" "+div.xpath(".//div[@class='info']/p//span[@class='']/a/text()")
            item["books_price"] = div.xpath(".//div[@class='action-buttons']/span/text()")
            item["books_category"] = div.xpath(".//span[@class='category']/span[@class='labeled-text']/span/text()")[0]
            item["books_detail"] = div.xpath(".//div[@class='article-desc-brief']/text()")
            item["books_imgs"] = div.xpath(".//div[@class='cover shadow-cover']/a/img/@src")
            book_list.append(item)
        return book_list

    def save_content_list(self,content_lists):
        with open('douban_readbook.json','a',encoding='utf-8') as f:
            for content in content_lists:
                f.write(json.dumps(content,ensure_ascii=False))
                f.write("\n")
            print("保存成功")

    def run(self):
        # 1.根据url地址的规律，构造url list
        urls = self.get_url_list()
        # 2.发送请求，获取响应
        for url in urls:
            content_lists = self.parse_url_list(url)
        # 3.提取数据
            content = self.get_content_url(content_lists)

        # 4.保存数据
            self.save_content_list(content)

if __name__ == '__main__':
    douban_readbooks = Douban_Readbook_Spider()
    douban_readbooks.run()