from django.shortcuts import render
from django.views.decorators.cache import cache_page
from django.views.decorators.csrf import ensure_csrf_cookie


class CartItem(object):
    """购物车中的商品项"""

    def __init__(self, sku, amount=1, selected=False):
        self.sku = sku
        self.amount = amount
        self.selected = selected

    @property
    def total(self):
        return self.sku.price * self.amount


class ShoppingCart(object):
    """购物车"""

    def __init__(self):
        self.items = {}
        self.index = 0

    def add_item(self, item):
        if item.sku.id in self.items:
            self.items[item.sku.id].amount += item.amount
        else:
            self.items[item.sku.id] = item

    def remove_item(self, sku_id):
        if sku_id in self.items:
            self.items.remove(sku_id)

    def clear_all_items(self):
        self.items.clear()

    @property
    def cart_items(self):
        return self.items.values()

    @property
    def cart_total(self):
        total = 0
        for item in self.items.values():
            total += item.total
        return total


@ensure_csrf_cookie
@cache_page(cache='page', timeout=300)
def home(request):
    if 'cart' not in request.session:
        request.session['cart'] = ShoppingCart()
    return render(request, 'index.html', {})
