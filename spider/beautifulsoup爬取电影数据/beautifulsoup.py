import json

import requests
import time
from bs4 import BeautifulSoup


class Bs_films():

    def __init__(self,url,headers):
        self.url = url
        self.headers = headers

    def get_one_page(self):
        response = requests.get(self.url,headers=self.headers).text
        soup = BeautifulSoup(response,'lxml')
        return soup

    def parse_page(self,html):

        info = html.find_all(name='dd')

        for item in info:
            film = {}
            film["index"] = [i.string for i in list(item.find(name='i'))][0]
            film["img"] = [img['data-src'] for img in item.select('.board-img')][0]
            film['title'] = [t.string for t in item.select('.name a')][0]
            film['score'] = [a.string for a in item.select('.star')][0]
            film['date'] = [d.string for d in item.select('.releasetime')][0]
            film['score'] = [(s1.string+s2.string) for s1,s2 in item.select('.score')][0]
            yield film



    def save_file(self,data):
        with open('bs_film.txt','a',encoding='utf-8') as f:
            f.write(json.dumps(data,ensure_ascii=False)+'\n')




def main(offset):
    HEADERS = {
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:2.0b13pre) Gecko/20110307 Firefox/4.0b13pre"
    }

    URL = 'http://maoyan.com/board/4?offset=%d'%offset

    film = Bs_films(URL, HEADERS)
    html = film.get_one_page()
    time.sleep(2)
    for data in film.parse_page(html):
        film.save_file(data)



if __name__ == '__main__':
    for i in range(10):
        main(i*10)
        time.sleep(1)







