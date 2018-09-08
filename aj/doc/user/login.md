### 登录接口

#### 请求
    — request GET /user/my_login/
#### 请求参数
    — phone str 电话
    — passwd str 密码
#### 响应
    — code 响应码
    — msg 响应信息
#### 响应参数
    — 'code':1006,'msg':'请填写完整参数'
    — 'code':1007,'msg':'手机号不符合规范'
    — 'code':1008,'msg':'登录用户不存在,请去注册'
    — 'code':1009,'msg':'密码错误，请重输'
