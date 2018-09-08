import random
import re
import os
from flask import Blueprint, redirect, \
    render_template, request, url_for, jsonify,session
from app.models import db, User
from utils import status_code
from utils.functions import is_login
from utils.settings import UPLOAD_DIR


# 初始化蓝图对象

user_blueprint = Blueprint('user',__name__)

# 迁移数据表
@user_blueprint.route('/')
def create_all():
    db.create_all()
    return '创建数据库成功'

# 注册（返回页面）
@user_blueprint.route('register/',methods=['GET'])
def register():
    if request.method == 'GET':
        return render_template('register.html')


# 实现注册
@user_blueprint.route('register/',methods=['POST'] )
def my_register():
    # 获取注册页面ajax提交过来的参数：request.form
    mobile = request.form.get('mobile')
    imagecode = request.form.get('imagecode')
    passwd = request.form.get('passwd')
    passwd2 = request.form.get('passwd2')

    # 校验是否填写完整
    if not all([mobile,imagecode,passwd,passwd2]):
        return jsonify(status_code.USER_REGISTER_PARAMS_NOT_EXISTS)
    # 校验手机号
    if not re.match(r'^1[345678]\d{9}$',mobile):
        return jsonify(status_code.USER_REGISTER_PHONE_IS_NOT_VALID)

    # 校验图片验证码
    if session.get('code') != imagecode:
        return jsonify(status_code.USER_REGISTER_CODE_IS_NOT_VALID)

    # 校验密码
    if passwd != passwd2:
        return jsonify(status_code.USER_REGISTER_PASSWORD_IS_NOT_EQUAL)

    # 判断手机是否注册
    user = User.query.filter(User.phone==mobile).all()
    if user:
        return jsonify(status_code.USER_REGISTER_PHONE_IS_EXISTS_ALREADY)
    # 保存用户的注册信息
    user = User()
    user.phone = mobile
    user.name = mobile
    user.password = passwd
    user.add_update()
    return jsonify(status_code.SUCCESS)
#
@user_blueprint.route('img_code/')
def img_code():
    # 获取验证码
    s = '1234567890qwertyuiopasdfghjklzxcvbnm'
    code = ''
    for _ in range(4):
        code += random.choice(s)
    # 将状态码存放在session中
    session['code'] = code
    return jsonify({'code':200,'msg':'请求成功','data':code})



# 登录(页面)
@user_blueprint.route('login/',methods=['GET'])
def login():
    if request.method == "GET":
        return render_template('login.html')

# 实现登录
@user_blueprint.route('my_login/',methods=['GET'])
def my_login():
    if request.method == "GET":
        # 获取手机号和密码
        phone = request.args.get('mobile')
        passwd = request.args.get('passwd')

        # 校验参数是否完整
        if not all([phone,passwd]):
            return jsonify(status_code.USER_LOGIN_PARAMS_NOT_EXISTS)

        # 校验手机号是否符合规格
        if not re.match(r'^1[345678]\d{9}$',phone):
            return jsonify(status_code.USER_LOGIN_PHONE_IS_NOT_VALID)
        # 判断手机号是否存在
        user = User.query.filter(User.phone==phone).first()
        if not user:
            return jsonify(status_code.USER_LOGIN_IS_NOT_EXISTS)
        # 判断密码是否正确
        if not user.check_pwd(passwd):
            return jsonify(status_code.USER_LOGIN_PASSWORD_IS_VALID)
        # 记录用户登录成功
        session['user_id'] = user.id
        return jsonify(status_code.SUCCESS)


@user_blueprint.route('my/',methods=['GET'])
@is_login
def my():
    if request.method == "GET":
        return render_template('my.html')


@user_blueprint.route('my_info/',methods=['GET'])
def my_info():
    user_id = session['user_id']
    user = User.query.get(user_id)
    user_info = user.to_basic_dict()
    return jsonify(user_info=user_info,code=status_code.SUCCESS)

# def log(func):
#     user_id = session.get('user_id')
#     user = User.query.get(user_id)

@user_blueprint.route('logout/',methods=['GET'])
@is_login
def logout():
    session.clear()
    return jsonify(status_code.SUCCESS)

@user_blueprint.route('profile/',methods=['GET'])
@is_login
def profile():
    return render_template('profile.html')



@user_blueprint.route('profile/',methods=['PATCH'])
def my_profile():
    # 获取头像

    avatar = request.files.get('avatar')
    user_id = session['user_id']

    if avatar:
        # 保存用户头像，保存在media
        # 保存图片到/static/media/upload/xxx.jpg
        avatar.save(os.path.join(UPLOAD_DIR,avatar.filename))
        # 修改用户的头像字段
        user = User.query.get(user_id)
        upload_avater_path = os.path.join('upload',avatar.filename)
        user.avatar=upload_avater_path
        user.add_update()
        return jsonify(code = status_code.SUCCESS,img_avatar=upload_avater_path)
    else:
        return jsonify(status_code.USER_PROFILES_AVATAR_NOT_EXISTS)

# @user_blueprint.route('orders/',methods=['GET'])
# def my_order():
#     return render_template('orders.html')


@user_blueprint.route('profile_name/',methods=['PATCH'])
def profile_name():
    # 修改用户名
    username = request.form.get('username')
    if not User.query.filter(User.name==username).count():
        user = User.query.get(session['user_id'])
        user.name = username
        user.add_update()
        return jsonify(status_code.SUCCESS)
    else:
        return jsonify(status_code.USERNAME_IS_ALREADY_EXISTS)

    # 获取用户名，校验用户名是否存在
    # 更新用户名


@user_blueprint.route('auth/',methods=['GET'])
@is_login
def auth():
    return render_template('auth.html')


@user_blueprint.route('auth/',methods=['PATCH'])
def my_auth():
    # 获取用户名和身份证号
    # 校验参数

    real_name = request.form.get('real_name')
    id_card = request.form.get('id_card')
    if not all([real_name,id_card]):
        return jsonify(status_code.USER_AUTH_PARAMS_IS_NOT_VALID)
    if not re.match(r'^[1-9]\d{16}[1-9X]$',id_card):
        return jsonify(status_code.USER_AUTH_ID_CARD_IS_NOT_VALID)

    # 修改用户的信息
    user = User.query.get(session['user_id'])
    user.id_card = id_card
    user.id_name = real_name
    user.add_update()
    return jsonify(status_code.SUCCESS)


@user_blueprint.route('auth_info/',methods=['GET'])
@is_login
def auth_info():
    user = User.query.get(session['user_id'])
    user_info = user.to_auth_dict()
    return jsonify(user_info=user_info,code=status_code.SUCCESS)

























































