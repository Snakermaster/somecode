import requests,time
from lxml import etree

def show_info(html):
    s = etree.HTML(html)
    house_info = s.xpath('//*[@id="page_list"]/ul/li')
    time.sleep(1)
    for div in house_info:

        title = div.xpath('./div[2]/div/a/span/text()')[0]
        price = div.xpath('./div[2]/span[1]/i/text()')[0]
        desc = div.xpath('./div[2]/div/em/text()')[0].strip()
        img = div.xpath('./a/img/@lazy_src')[0]
        time.sleep(1)
        print("地点:{}\n价格:{}\n描述:{}\n图片:{}\n".format(title,price,desc,img))



def main():
    with open(r'C:\Users\Administrator\PycharmProjects\untitled2\json\租房信息.txt','w',encoding='utf-8') as f:
        for i in range(1,6):
            url = 'http://cd.xiaozhu.com/search-duanzufang-p{}-0/'.format(i)
            headers = {
                "User-Agent": "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; 360SE)"
            }
            response = requests.get(url,headers=headers).text
            # show_info(response)
            s = etree.HTML(response)
            house_info = s.xpath('//*[@id="page_list"]/ul/li')
            time.sleep(1)
            for div in house_info:
                title = div.xpath('./div[2]/div/a/span/text()')[0]
                price = div.xpath('./div[2]/span[1]/i/text()')[0]
                desc = div.xpath('./div[2]/div/em/text()')[0].strip()
                img = div.xpath('./a/img/@lazy_src')[0]
                time.sleep(1)
                f.write("地点:{}\n价格:{}\n描述:{}\n图片:{}\n".format(title,price,desc,img))





if __name__ == '__main__':
    main()