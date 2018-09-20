

from datetime import datetime, timedelta
from django.contrib.auth.hashers import make_password, check_password
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from users.models import UserModel, UserTicketModel
from home.models import OrderModel
from utils.function import random_ticket
# Create your views here.


# 个人中心
def mine(request):
    if request.method == 'GET':
        wait_pay = ''
        paid = ''
        user = request.user
        if user.id:
            wait_pay = OrderModel.objects.filter(user=user,o_status=0).count()
            paid = OrderModel.objects.filter(user=user, o_status=1).count()
        return render(request, 'mine/mine.html', {'wait_pay': wait_pay, 'paid': paid},)

# 注册
def register(request):
    if request.method == "GET":
        return render(request,'user/user_register.html')
    if request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        # 获取图片，enctype,MEDIA_URL,MEDIA_ROOT
        icon = request.FILES.get('icon')
        # 验证所有参数是否填写完整
        if not all([username,email,password,icon]):
            error = {'msg':'参数不能为空'}
            return render(request,'user/user_register.html',error)

        # 验证用户是否被注册过
        user = UserModel.objects.filter(username=username)
        if user:
            error = {'msg':'该用户名已被注册，请直接登录'}
            return render(request,'user/user_register.html',error)

        # 创建用户
        UserModel.objects.create(username=username,password=make_password(password),
                                 email=email,icon=icon)


        return HttpResponseRedirect(reverse('user:login'))

# 登录

def login(request):
    if request.method == "GET":
        return render(request,'user/user_login.html')
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        # 校验参数

        if not all([username,password]):
            error = '请填写完整信息'
            return render(request,'user/user_login.html',{'error':error})
        # 判断用户是否存在
        user = UserModel.objects.filter(username=username).first()
        if not user:
            error = '该用户不存在，请保证用户名正确！'
            return render(request,'user/user_login.html',{'error':error})
        # 判断密码是否正确
        if not check_password(password,user.password):

            error = '密码错误'
            return render(request,'user/user_login.html',{'error':error})
        # 设置ticket值与过期时间和cookie
        res = HttpResponseRedirect(reverse('user:mine'))
        ticket = random_ticket()
        out_time = datetime.now() + timedelta(days=1)
        res.set_cookie('ticket',ticket,expires=out_time)
        # 服务端保存以上值
        UserTicketModel.objects.create(ticket=ticket,
                                       out_time=out_time,
                                       user=user)


        return res



# 个人中心

def mine(request):
    if request.method == "GET":
        return render(request, 'mine/mine.html' )

# 退出登录
def logout(request):
    if request.method == "GET":

        # 删除cookie中的值
        res = HttpResponseRedirect(reverse('user:mine'))
        res.delete_cookie('ticket')
        # res.set_cookie()

        return res



