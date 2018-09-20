from django.shortcuts import render
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt

from home.models import MainWheel, MainNav, MainMustBuy, MainShop, MainShow, FoodType, Goods, CartModel,OrderModel,OrderGoodsModel
from django.http import HttpResponseRedirect, JsonResponse


# Create your views here.
from utils.function import get_order_number


def index(request):
    if request.method == "GET":
        mainwheels = MainWheel.objects.all()
        mainnavs = MainNav.objects.all()
        mainmustbuys = MainMustBuy.objects.all()
        mainshops = MainShop.objects.all()
        mainshows = MainShow.objects.all()


        data = {
            'mainwheels': mainwheels,
            'mainnavs': mainnavs,
            'mainmustbuys': mainmustbuys,
            'mainshops': mainshops,
            'mainshows': mainshows,
        }

        return render(request,'home/home.html',data)
def market(request):
    if request.method == "GET":

        return HttpResponseRedirect(reverse('home:market_params',kwargs={'typeid':104749,
                                                                         'cid':0,
                                                                         'sid':0}))


def market_params(request,typeid,cid,sid):
    if request.method == "GET":
        # 分类
        foodtypes = FoodType.objects.all()
        # 分类对应的商品信息
        if cid == '0':
            goods = Goods.objects.filter(categoryid=typeid)
        else:
            goods = Goods.objects.filter(categoryid=typeid,childcid=cid)
        if sid == '0':
            pass
        elif sid == '1':
            goods = goods.order_by('-productnum')
        elif sid == '2':
            goods = goods.order_by('-price')
        elif sid == '3':
            goods = goods.order_by('price')



        # 获取某个分类的全部类型
        types = FoodType.objects.filter(typeid=typeid).first()
        childtypes = [i.split(':') for i in types.childtypenames.split('#')]

        data = {
            'foodtypes':foodtypes,
            'goods':goods,
            'typeid':typeid,
            'childtypes':childtypes,
            'cid':cid,
            'sid':sid
        }

        return render(request,'market/market.html',data)


# 添加商品
@csrf_exempt
def add_To_Cart(request):
    if request.method == "POST":
        user = request.user
        if user.id:
            goods_id = request.POST.get('good_id')

            cart = CartModel.objects.filter(user=user,goods_id=goods_id).first()

            if cart:
                cart.c_num += 1
                cart.save()
                c_data = {'c_num':cart.c_num}

            else:
                CartModel.objects.create(user=user, goods_id=goods_id)
                c_data = {'c_num':1}

            data = {
                'code':200,
                'msg':'请求成功',
                'data': c_data,
            }
            return JsonResponse(data)
        else:
            data = {
                'code':201,
                'msg':'请先登录',
            }
            return JsonResponse(data)

# 删除商品
@csrf_exempt
def desc_To_Cart(request):
    if request.method == "POST":
        # 先验证用户是否存在
        # 验证用户删除的商品是否在购物车中出现
        # 如果购物车中有，验证c_num是否为1，为1则删除数据。否则c_num自减一
        user = request.user

        if user.id:

            goods_id = request.POST.get('goods_id')
            cart = CartModel.objects.filter(user=user,goods_id=goods_id).first()
            if cart:
                if cart.c_num ==1:
                    cart.delete()
                    c_data = {'c_num': 0}

                else:
                    cart.c_num -=1
                    cart.save()
                    c_data = {'c_num': cart.c_num}
                data = {
                    'code': 200,
                    'msg': '请求成功',
                    'data': c_data,
                }

                return JsonResponse(data)
        else:
            data = {
                'code': 201,
                'msg': '请先登录',
                'data': ''
            }

            return JsonResponse(data)
# 刷新商品
def refresh_goods(request):
    if request.method == "GET":
    # 获取当前登录的人
    # 查询购物车中用户对应的购物车数据，并返回
    # 如果购物车中有数据，则返回商品的id值，和商品的数量
        user = request.user
        data = {}
        data['code'] = 200
        data['msg'] = '请求成功'
        if user.id:
            carts = CartModel.objects.filter(user=user)
            if carts:
                cart_data = [(cart.goods_id,cart.c_num) for cart in carts ]
                data['data'] = cart_data

            return JsonResponse(data)

        else:
            data = {
                'code': 101,
                'msg': '请先登录',
            }
            return JsonResponse(data)

# 购物车
def cart(request):
    if request.method == "GET":
        # 验证是否有用户登录
        user = request.user
        if user.id:
            carts = CartModel.objects.filter(user=user)
            return render(request,'cart/cart.html',{'carts':carts})
        else:
            return HttpResponseRedirect(reverse('user:login'))

# 购物车勾选商品
@csrf_exempt
def change_cart_goods(request):
    if request.method == "POST":
        user = request.user
        goods_id = request.POST.get('goods.id')
        cart = CartModel.objects.filter(user=user,goods_id=goods_id).first()
        if cart.is_select:
            cart.is_select = False
            cart.save()
        else:
            cart.is_select = True
            cart.save()
        # 查询当前用户的购物车中是否有没有被选择的商品，如果有，则页面全选为空
        if CartModel.objects.filter(is_select=False).exists():
            all_select = False
        else:
            all_select = True

        return JsonResponse({'code': 200, 'msg': '请求成功',
                            'is_select': cart.is_select,
                            'all_select': all_select})

def change_all_cart_goods(request):
    if request.method == 'POST':
        user =request.user
        # 修改购物车中所有商品的状态, 1表示全选，0表示全不选
        all_select = request.POST.get('all_select')
        if all_select == '1':
            CartModel.objects.filter(user=user).update(is_select=True)
        else:
            CartModel.objects.filter(user=user).update(is_select=False)
        carts_goods_id = CartModel.objects.filter(user=user).values('goods_id')
        all_goods_id = [i['goods_id'] for i in carts_goods_id]
        return JsonResponse({'code': 200, 'msg': '请求成功', 'all_goods_id': all_goods_id})

def goods_count(request):
    if request.method == "GET":
        user = request.user
        carts = CartModel.objects.filter(user=user,is_select=True)
        sum = 0
        for cart in carts:
            sum += cart.c_num * cart.goods.price
            sum = round(sum, 3)
        return JsonResponse({'code':200,'msg':'请求成功','data':sum})


def order(request):
    if request.method == "POST":
        # 创建订单
        # 创建订订单和商品的详情表
        # 将订单中已经下单的商品删除
        # 获取用户
        user = request.user
        # 获取订单编号
        o_num = get_order_number()
        # 创建订单
        order = OrderModel.objects.create(user=user,o_num=o_num )
        # 获取购物车中已选择的商品
        carts = CartModel.objects.filter(user=user,is_select=True)
        # 创建商品和订单的详情表
        for cart in carts:
            OrderGoodsModel.objects.create(order=order,
                                           goods=cart.goods,
                                           goods_num=cart.c_num)
        # 删除购物车中已下单的信息
        carts.delete()
        return JsonResponse({'code':200,'msg':'请求成功','order_id':o_num})


def order_info(request):
    if request.method == "GET":
        order_id = request.GET.get('order_id')
        order = OrderModel.objects.filter(o_num=order_id).first()
        return render(request, 'order/order_info.html', {'order': order})


def order_pay(request):
    if request.method == "POST":
        order_id = request.POST.get('order_id')
        order = OrderModel.objects.filter(o_num=order_id).first()
        order.o_status = 1
        order.save()
        return JsonResponse({'code': 200, 'msg': '请求成功'})



def wait_to_pay(request):
    if request.method == "GET":

        user = request.user
        orders = OrderModel.objects.filter(user=user,o_status=0)
        return render(request,'order/order_list_wait_pay.html',
                      {'orders':orders})

def paid(request):
    if request.method == "GET":
        user = request.user
        orders = OrderModel.objects.filter(user=user,o_status=1)
        return render(request,'order/order_list_payed.html',
                      {'orders':orders})








