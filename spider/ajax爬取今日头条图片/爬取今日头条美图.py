import time
from hashlib import md5
import requests
from urllib.parse import urlencode
import os



### 要爬取的网站信息


'''
https://www.toutiao.com/search_content/?offset=0&format=json&keyword=%E7%BE%8E%E5%A5%B3&autoload=true&count=20&cur_tab=3&from=gallery

'''

### 获取单页信息


def get_one_page(offset):
	params = {
		"offset":offset,
		"format":'json',
		"keyword":"美女",
		"autoload":"true",
		"count":20,
		"cur_tab":"3",
		"from":"gallery"
	}
	url = "https://www.toutiao.com/search_content/?" + urlencode(params)

  headers = {
  "Host": "www.toutiao.com",
  "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:43.0) Gecko/20100101 Firefox/43.0",
  "Accept-Language": "zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3",
  "Accept-Encoding": "gzip, deflate",
  "Connection": "keep-alive"
  }
  response = requests.get(url,headers=headers)
  if response.status_code == 200:
  	return response.json()
  else:
  print('获取失败')

### 解析单页信息
def parser_data(json):
	if json.get('data'):
		for item in json.get('data'):
		title = item.get("title")
		images = item.get("image_list")
		for images in images:
	    yield {
	    "title" : title,
	    "image" : images.get('url')
	    }

### 保存信息

def save_data(data):
	if not os.path.exists(data.get('title')):
	os.mkdir(data.get('title'))
	try:
		response = requests.get('http:'+data.get('image')) 
		# print(response)        
		if response.status_code == 200:
		file_path = '{0}/{1}.{2}'.format(data.get('title'),md5(response.content).hexdigest(),'jpg')
	    if not os.path.exists(file_path):
	    with open(file_path,'ab') as f:
	    f.write(response.content)
	    else:
	    print('Already Download', file_path)

except requests.exceptions.MissingSchema :
print('请等待三秒')
time.sleep(2)


### 获取单页信息
data = get_one_page(0)
### 获取单页解析数据
data2 = parser_data(data)
### 保存图片信息
for data3 in data2:
    save_data(data3)
### 保存成功
print('保存成功')

### 获取多页信息

for i in range(10):
	data = get_one_page(i*20)
	data2 = parser_data(data)
	for data3 in data2:
	save_data(data3)
	print('保存成功')



