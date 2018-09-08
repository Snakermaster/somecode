### 首页个人信息接口

#### 请求
    — request GET /user/my_info

#### 请求参数
    — user_id int 当前登录用户id
    — user object 当前登录用户对象
    — user_info dict 序列化当前用户对象

#### 响应
    — code 响应码
    — msg 响应信息

#### 响应参数
    — user_info 序列化当前用户对象
    — 'code':200,'msg':'请求成功'