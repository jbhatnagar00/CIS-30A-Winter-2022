class Grocery:
    def __init__(self):
        self.grocery_items = []
        self.grocery_price = []
        self.itme_price_dict = {}

        self.grocery_items = ['Eggs', 'Chicken', 'Tomato', 'Milk', 'Butter', 'Beans', 'Fruit Juice',
                              'Coffee', 'Rice', 'Crackers', 'Chips', 'Banana', 'Oranges'] #Items sold at store
        self.grocery_price = [2.49, 5.25, 2.25, 3.79, 2.99, 1.25, 1.25,
                              6.49, 3.45, 2.15, 3.45, 1.75, 2.25] #Prices in the same order as grocery_items


    def make_item_price_dict(self):
        for gi, ip in zip(self.grocery_price, self.grocery_items):
            self.itme_price_dict[ip] = gi
        return self.itme_price_dict
