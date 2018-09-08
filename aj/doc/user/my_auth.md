### 实名认证接口

#### 请求
    — request PATCH /user/auth/

#### 请求参数
    — real_name str 用户实名
    — id_card str 用户身份证
    — user object 当前登录用户
    — user.id_card str 用户身份证号
    — user.id_name str 用户实名

#### 响应
    — code 响应码
    — msg 响应信息

#### 响应参数
    — 'code':1012,'msg':'请填写完整信息'
    — 'code':1013,'msg':'无效的身份证号'
    — 'code':200,'msg':'请求成功'