import redis
from flask import session,redirect,url_for
from functools import wraps

from flask_session import Session

from app.models import db
from utils.settings import MYSQL_DATABASES, REDIS_DATABASES


def is_login(func):
    @wraps(func)
    def check_status(*args,**kwargs):
        try:
            user_id = session['user_id']
        except:
            return redirect(url_for('user.login'))
        return func(*args,**kwargs)
    return check_status


def init_ext(app):
    #  绑定SQLALCHEMY和app
    db.init_app(app)
    # 绑定Session 和app
    se = Session()
    se.init_app(app)

def get_mysqldb_url():
    driver = MYSQL_DATABASES['DRIVER']
    DH = MYSQL_DATABASES['DH']
    HOST = MYSQL_DATABASES['HOST']
    ROOT = MYSQL_DATABASES['ROOT']
    PORT = MYSQL_DATABASES['PORT']
    PASSWORD = MYSQL_DATABASES['PASSWORD']
    NAME = MYSQL_DATABASES['NAME']
    return '{}+{}://{}:{}@{}:{}/{}'.format(driver, DH, ROOT,
                                           PASSWORD, HOST, PORT, NAME)

def get_redisdb_url():
    HOST = REDIS_DATABASES['HOST']
    PORT = REDIS_DATABASES['PORT']

    return redis.Redis(host=HOST,port=PORT)






