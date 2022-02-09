from datetime import date
from grocery import Grocery


class GroceryPurchased(Grocery):
    def __init__(self, purchased_items_dict):
        super().__init__()
        self.purchased_items_dict = purchased_items_dict
        self.item_details_dict = super().make_item_price_dict()
        self.bill_dict = {}

    def get_price_for_an_item(self):
        for k, v in self.purchased_items_dict.items(): # k is item purchased and v is quantity
            price_of_item = self.item_details_dict[str(k).title()]
            sub_total = price_of_item * int(v)
            self.bill_dict.update({k : (v, price_of_item , sub_total)})
        return self.bill_dict

    def generate_bill_statement(self):
        print()
        print('-'* 60)
        print("\nJason's Grocery Store") #Start of order summary
        print("1234 Nonexistant St")
        print("Imaginary Town, CA, 9221")
        print('\n')
        print("Purchase Date:", date.today())
        print('-'* 60)
        str_a = 'Item'
        str_b = 'Rate'
        str_c = "Quantity"
        str_d = '    Subtotal'
        print("{:<20}{:^10}{:>10}{:>10}".format(str_a, str_b, str_c, str_d))
        print('-' * 60)
        total = 0.0
        for k, v in self.bill_dict.items():
            #Item name is the key of this dictionary, and value part is a tuple consisting of Rate, Quantity, and Subtotal
            itm_name = str(k)
            itm_qty = int(v[0])
            itm_rate = float(v[1])
            itm_subttl = float(v[2])
            total += itm_subttl
            print("{:<20}{:^10}{:>7}{:>13}".format(itm_name, "$" + str(itm_rate), itm_qty, "${:.2f}".format(itm_subttl)))
        print('-' * 60)
        print("Total Amount:  ${:.2f}".format(total))
        print("Delivery Date:", date.today())
        print("\nHope to see you again!")
