### 发布房源接口

#### 请求
    — request POST /house/my_new_house/
#### 请求参数
    — data 简化 request.form
    — house object 房屋的实例化对象
    — house.user_id int 房屋对应的地区
    — house.title str 标题
    — house.price int 单价，单位：分
    — house.area_id int 房屋对应的用户
    — house.address str 地址
    — house.room_count int 房间数目
    — house.unit str 房屋单元
    — house.capacity str 房屋容纳的人数
    — house.beds int 房屋床铺的配置
    — house.deposit int 房屋押金
    — house.min_days int 最少入住天数
    — house.max_days int 最多入住天数，0表示不限制
    — facilities list 设施列表对象
    — facility object 设施对象
    — house.facilities.append(facility) 利用多对多关系添加房屋和设施关联
#### 响应
    — code 响应码
    — msg 响应信息
#### 响应参数
    — 'code':200,'msg':'请求成功'
