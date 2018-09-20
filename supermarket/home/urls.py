from django.conf.urls import url
from home import views


urlpatterns = [
# 首页
url(r'^index/',views.index,name='index'),
# 闪购页面
url(r'^market/',views.market,name='market'),
url(r'^market_params/(?P<typeid>\d+)/(?P<cid>\d+)/(?P<sid>\d+)/',views.market_params,name='market_params'),
# 添加商品
url(r'^add_To_Cart/',views.add_To_Cart,name='add_To_Cart'),
# 删除商品
url(r'^desc_To_Cart/',views.desc_To_Cart,name='desc_To_Cart'),
# 刷新闪购页面商品初始值
url(r'^refresh_goods/',views.refresh_goods,name='refresh_goods'),
# 购物车
url(r'^cart/',views.cart,name='cart'),

# 改变购物车中商品的勾选状态
url(r'^change_cart_goods/',views.change_cart_goods,name='change_cart_goods'),
# # 改变所有商品的勾选状态
url(r'^change_all_cart_goods/',views.change_all_cart_goods,name='change_all_cart_goods'),

# 计算总价
url(r'^goods_count/',views.goods_count,name='goods_count'),
# 订单
url(r'^order/',views.order,name='order'),
# 下单信息
url(r'^order_info/',views.order_info,name='order_info'),
# 下单支付
url(r'^order_pay/',views.order_pay,name='order_pay'),
# 待付款
url(r'^wait_to_pay/',views.wait_to_pay,name='wait_to_pay'),

# 付款未发货
url(r'^paid/',views.paid,name='paid'),


]