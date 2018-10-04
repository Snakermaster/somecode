import requests
from hashlib import md5


class Super_Eagle(object):

    def __init__(self,username,password,soft_id):
        self.username = username
        password = password.encode("utf-8")
        self.password = md5(password).hexdigest()
        self.soft_id = soft_id
        self.base_params = {

            "user" : self.username,
            "pass2" : self.password,
            "softid": self.soft_id
        }
        self.headers = {
            'Connection': 'Keep-Alive',
            'User-Agent': 'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0)',
        }
    def Post_img(self,im,codetype):
        params = {
            "codetype":codetype
        }
        params.update(self.base_params)
        files = {"userfile":('ccc.jpg',im)}
        r = requests.post('http://upload.chaojiying.net/Upload/Processing.php',
                          data=params,files=files,headers=self.headers)
        return r.json()

    def ReportError(self,im_id):
        params = {
            "id":im_id
        }
        params.update(self.base_params)
        r = requests.post('http://upload.chaojiying.net/Upload/Processing.php',
                          data=params,headers=self.headers)
        return r.json()


if __name__ == '__main__':

    super_eagle = Super_Eagle('carmack', 'Vff635241', '96001')
    im = open('pic2.png', 'rb').read()
    print(super_eagle.Post_img(im, 3006))









