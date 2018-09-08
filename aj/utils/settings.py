import os
# 基础路径
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# TEMPLATES路径
TEMPLATES_DIR = os.path.join(BASE_DIR,'templates')

# STATIC路径
STATIC_DIR = os.path.join(BASE_DIR,'static')
# MEDIA路径
MEDIA_URL = os.path.join(STATIC_DIR,'media')
# UPLOAD路径
UPLOAD_DIR = os.path.join(MEDIA_URL,'upload')

# 数据库配置
MYSQL_DATABASES = {
    'DRIVER':'mysql',
    'DH':'pymysql',
    'ROOT':'root',
    'PASSWORD':'123456',
    'PORT':3306,
    'HOST':'127.0.0.1',
    'NAME':'aj'

}
REDIS_DATABASES = {
    'HOST':'127.0.0.1',
    'PORT':6379,

}


