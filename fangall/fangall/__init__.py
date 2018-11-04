import os

import pymysql
import celery

from celery.schedules import crontab
from django.conf import settings

pymysql.install_as_MySQLdb()

# 注册环境变量 - 让Celery能够读取项目的配置文件
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'fangall.settings')

# 创建Celery实例并指定消息中间人(RabbitMQ)的URL
app = celery.Celery('fangall',
                    broker='amqp://snaker:123456@120.77.249.236:5672/vhost1')

# 从项目的配置文件读取Celery配置信息
app.config_from_object('django.conf:settings')
# 从指定的文件(例如celery_config.py)中读取Celery配置信息
# app.config_from_object('celery_config')

# 让Celery自动从参数指定的应用中发现异步任务/定时任务
app.autodiscover_tasks(['common'])
# 让Celery自动从所有注册的应用中发现异步任务/定时任务
# app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)

# 配置定时任务（计划任务）
app.conf.update(
    timezone=settings.TIME_ZONE,
    enable_utc=True,
    # celery -A fangall beat -l debug & - 启动消息生产者
    # 定时任务（计划任务）相当于是消息的生产者
    # 如果只有生产者没有消费者那么消息就会在消息队列中积压
    # celery -A fangall worker -l debug & - 启动消息消费者
    # 将来实际部署项目的时候生产者、消费者、消息队列可能都是不同节点
    beat_schedule={
        'task1': {
            'task': 'common.tasks.show_msg',
            'schedule': crontab(),
            'args': ('刘强东，奶茶妹妹喊你回家喝奶啦', )
        },
        'task2': {
            'task': 'common.tasks.foo',
            'schedule': crontab(),
            'args': ('Just a Test',)
        }
    },
)
