#### 用户信息接口

#### 请求
    — request GET /user/auth_info/
#### 请求参数
    — user object 当前登录对象
    — user_info dict 序列化用户对象
#### 响应
    — code 响应码
    — msg 响应信息
#### 响应参数
    — 'code':200,'msg':'请求成功'
    — user_info dict 序列化的用户对象