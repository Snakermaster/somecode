### 判断实名房源接口

#### 请求
    — request GET /house/house_info/
#### 请求参数
    — user object 当前登录用户
    — house object 当前用户的房屋信息
    — house_info dict 序列化房屋信息
#### 响应
    — code 响应码
    — msg 响应信息
    — OK 200参数
#### 响应参数
    — house_info dict 序列化的房屋信息
    — OK 200 响应码
    — 'code':1014,'msg':'用户没有实名认证'

