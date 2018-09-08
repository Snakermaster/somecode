### 地区和设施接口

#### 请求
    — request GET /house/area_facility/
#### 请求参数
    — areas object 地区对象列表
    — facilities object 设备对象列表
    — area_info dict 序列化的地区对象
    — facility_info dict 序列化的设施参数
#### 响应
    — code 响应码
    — msg 响应信息
    — OK 200响应码
#### 响应参数
    — area_info dict 序列化的地区参数
    — facility_info dict 序列化的设施参数
    — code -> OK 200 响应码