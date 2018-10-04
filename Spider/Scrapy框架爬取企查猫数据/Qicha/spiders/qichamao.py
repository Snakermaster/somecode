# -*- coding: utf-8 -*-
from urllib.parse import urlencode
import json
from Qicha.items import QichaItem
from Qicha.random_agent import get_random_agent
import scrapy
'''
https://www.qichamao.com/cert-wall

'''

class QichaSpider(scrapy.Spider):
    name = 'qichamao'
    allowed_domains = ['www.qichamao.com']
    start_urls = ['http://www.qichamao.com/cert-wall']


    def start_Request(self):
        agent = get_random_agent()
        data = {'pagesize':9}
        base_url = 'https://www.qichamao.com/cert-wall'

        headers = {
            'Referer': 'https://www.qichamao.com/cert-wall/',
            'User-Agent': agent,
            'Host': 'www.qichamao.com',
            'Accept': 'application/json, text/plain, */*',
            'Accept-Encoding': 'gzip, deflate, sdch',
            'Accept-Language': 'zh-CN,zh;q=0.8,en;q=0.6,ja;q=0.4,zh-TW;q=0.2,mt;q=0.2',
            'Connection': 'keep-alive',
            'X-Requested-With': 'XMLHttpRequest',

        }
        for page in range(2,self.settings.get('MAX_PAGE')+1):
            print('*'*20)
            print(page)
            data['page'] = str(page)
            yield scrapy.FormRequest(url=base_url,headers=headers,
                                    method='POST',formdata = data,
                                    callback=self.parse)

    def parse(self, response):
        data = json.loads(response.text)
        for item in data.get('dataList'):
            company = QichaItem()
            company['company_name']=item.get('CompanyName')
            company['tell'] = item.get('c_phone')
            yield company
