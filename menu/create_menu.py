import datetime
from menu.models import Menu, Item

CART_ID = 'CART-ID'

class ItemAlreadyExists(Exception):
    pass

class ItemDoesNotExist(Exception):
    pass

class Menus:
    def __init__(self, request):
        cart_id = request.session.get(CART_ID)
        if cart_id:
            try:
                menu = Menu.objects.get(id=cart_id)
            except Menu.DoesNotExist:
                menu = self.new(request)
        else:
            menu = self.new(request)
        self.menu = menu

    def __iter__(self):
        for item in self.menu.item_set.all():
            yield item

    def new(self, request):
        menu = Menu(creation_date=datetime.datetime.now())
        menu.save()
        request.session[CART_ID] = menu.id
        return menu

    def add(self, product):
        try:
            item = Item.objects.get(
                menu=self.menu,
                product=product,
            )
        except Item.DoesNotExist:
            item = Item()
            item.menu = self.menu
            item.product = product
            item.save()
        else: #ItemAlreadyExists
            item.save()

    def remove(self, product):
        try:
            item = Item.objects.get(
                menu=self.menu,
                product=product,
            )
        except Item.DoesNotExist:
            raise ItemDoesNotExist
        else:
            item.delete()

    def update(self, product):
        try:
            item = Item.objects.get(
                menu=self.menu,
                product=product,
            )
        except Item.DoesNotExist:
            raise ItemDoesNotExist

    def clear(self):
        for item in self.menu.item_set.all():
            item.delete()
