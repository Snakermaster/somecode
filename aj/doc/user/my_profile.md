### 头像上传接口


#### 请求
    — request PATCH /user/profile/
#### 请求参数
    — avatar str 头像
    — user_id int 用户id
    — user object 用户对象
    — upload_avater_path 图片上传路径
    — user.avatar 用户头像
#### 响应

    — code 响应码
    — msg 响应信息

#### 响应参数

    — 'code':200,'msg':'请求成功'
    — 'code':1010,'msg':'请选择头像'
