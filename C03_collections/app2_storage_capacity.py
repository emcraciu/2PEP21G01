"""We need a class for an object that will keep track of products in a virtual supermarket for a game that has a
limited number of separated shelves. Processing needs  to be done quickly.
  - new product s will be listed first
  - once a product has been sold out wit will not longer be displayed
  - when there is no more room on shelves products are stored for later
  - when a customer returns a product it will be first product displayed"""
from collections import deque
import random


class Shop:
    shop_items = deque(maxlen=4)
    waiting_list = []

    def add_products(self, new_product):
        if len(self.shop_items) < 4:
            self.shop_items.appendleft(new_product)
        else:
            self.waiting_list.append(new_product)

    def list_products(self):
        print(self.shop_items)

    def sell_products(self, prod_name):
        self.shop_items.remove(prod_name)
        self.shop_items.appendleft(self.waiting_list.pop())

    def return_product(self, prod_name):
        self.add_products(prod_name)


if __name__ == '__main__':

    shop1 = Shop()

    for i in range(10):
        shop1.add_products("product" + str(i))

    shop1.sell_products(shop1.shop_items[random.randint(0, len(shop1.shop_items) - 1)])
    print(shop1.waiting_list)
    shop1.list_products()
    shop1.return_product("productx")
    shop1.sell_products(shop1.shop_items[random.randint(0, len(shop1.shop_items) - 1)])
    shop1.list_products()
