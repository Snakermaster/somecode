### 修改用户名接口
#### 请求
    — request PATCH /user/profile_name/
#### 请求参数
    — username str 用户名
    — user object 当前登录用户对象
    — user.name str 当前用户的名
#### 响应
    — code 响应码
    — msg 响应信息
#### 响应参数
    — 'code':200,'msg':'请求成功'
    — 'code':1011,'msg':'请更换用户名'





