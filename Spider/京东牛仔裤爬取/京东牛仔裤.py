import requests,time
from lxml import etree


def show_info(html):
    s = etree.HTML(html)
    info = s.xpath('//*[@id="J_goodsList"]/ul/li/div')
    # print(info)
    time.sleep(3)
    for div in info:
        title = div.xpath('./div[4]/a/em/text()')[0]
        price = div.xpath('./div[3]/strong/i/text()')[0]
        num = div.xpath('./div[5]/strong/a/text()')[0]
        img = div.xpath('./div[1]/a/img/@source-data-lazy-img')[0]
        time.sleep(1)

        print("名称: {}\n价格: {}\n评价人数: {}\n图片: {}\n".format(title,price,num,img))








def main():
    url = 'https://search.jd.com/Search?keyword=%E7%89%9B%E4%BB%94%E8%A3%A4%E7%94%B7&enc=utf-8&qrst=1&rt=1&stop=1&vt=2&page=7&s=159&click=0'
    headers = {

    }
    response = requests.get(url,headers=headers).content
    # print(response)
    show_info(response)
    time.sleep(1)


if __name__ == '__main__':
    main()







