### 注册接口

#### 请求

    — request POST /user/register/

#### 请求参数

    — mobile str 手机号

    — imagecode str 图片验证

    — passwd str 密码

    — passwd2 str 确认密码


#### 响应

    — code 响应码
    — msg 响应信息

#### 响应参数

    — 'code':1001,'msg':'请填写完整参数'

    — 'code':1002,'msg':'手机号不符合规范'

    — 'code':1003,'msg':'图片验证码错误'

    — 'code': 1004, 'msg': '密码不一致'

    — 'code':1005,'msg':'该手机号已注册，请直接登录'

