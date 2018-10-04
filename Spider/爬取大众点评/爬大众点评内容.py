import requests
from urllib.parse import urlencode









def Dzdp(id=1):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:2.0b13pre) Gecko/20110307 Firefox/4.0b13pre"
    }

    params = {
        'cityId': id
    }
    url = 'http://www.dianping.com/bar/search?' + urlencode(params)

    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            return response.json()
    except requests.ConnectionError as e:
        print('Error',e.args)



def Parse_data(data):

    for item in data['recordList']:
        yield {
            'location':item['valueMap']['location'],
            'type': item['valueMap']['suggestkeyword'],
            'datatype':item['valueMap']['datatype'],

        }

if __name__ == '__main__':
    for i in range(10):
        info = Dzdp(i)
        for item in list(Parse_data(info)):
            print(item)



