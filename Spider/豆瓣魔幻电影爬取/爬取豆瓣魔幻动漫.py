from urllib.parse import urlencode

import requests,time


def show_info(json):
    for i in range(20):
        dict_info = json["data"][i]
        name = dict_info["title"]
        rate = dict_info["rate"]
        actors = dict_info["casts"]
        img = dict_info["cover"]
        url = dict_info["url"]
        time.sleep(1)
        print("片名:{}\n评分:{}\n演员:{}\n封面图:{}\n地址:{}\n".
              format(name,rate,' '.join(actors),img,url))




'''

'https://movie.douban.com/j/new_search_subjects?sort=T&range=0,10&tags=%E9%AD%94%E5%B9%BB,%E5%8A%A8%E6%BC%AB&start=20'
'''


def main():
    try:
        with open(r'C:\Users\Administrator\PycharmProjects\untitled2\code\魔幻动漫.csv','w',encoding='utf-8') as f:
            for page in range(5):
                # print(page)
                params = {
                    "sort":"T",
                    "range":"0,10",
                    "tags":"魔幻,动漫",
                    "start":page*20,
                }
                url = 'https://movie.douban.com/j/new_search_subjects?'+urlencode(params)
                headers = {
                    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:2.0b13pre) Gecko/20110307 Firefox/4.0b13pre"
                }
                respones = requests.get(url,headers=headers).json()
                # print(respones)
                # show_info(respones)
                time.sleep(2)
                for i in range(20):
                    dict_info = respones["data"][i]
                    name = dict_info["title"]
                    rate = dict_info["rate"]
                    actors = dict_info["casts"]
                    img = dict_info["cover"]
                    url = dict_info["url"]
                    time.sleep(1)
                    f.write("{},{},{},{},{}\n".
                          format(name, rate, ' '.join(actors), img, url))
                    # print("片名:{}评分:{}演员:{}封面图:{}地址:{}".
                    #       format(name, rate, ' '.join(actors), img, url))
        print('保存成功')
    except:
        print('保存失败')





if __name__ == '__main__':
    main()


















