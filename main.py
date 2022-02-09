from grocery import Grocery
from grocery_purchase import GroceryPurchased

if __name__ == '__main__':
    #Welcome message for customer
    username = input("Please enter your name:\n") 
    welcome_message = "Hi {}, Welcome to Jason's Grocery Store".format(username)
    decorative_string = '-' * len(welcome_message)
    print(decorative_string)
    print(welcome_message)
    print(decorative_string)
    print("Here's what we are offering today!\n")
    print("Item\t\t\t   Price")
    print('-' * 40)


    g = Grocery()
    available_items = g.make_item_price_dict()
    #Get the max length of item in the list
    max_lnth = 0
    for k, v in available_items.items():
        if len(k) > max_lnth:
            max_lnth = len(k)
        # print(k, '\t\t\t', v)
    for k, v in available_items.items():
        print("{:<20}{:^20}".format(k, "$" + str(float(v))))

    shopping_cart = {}
    continue_shopping = input("\nDo you wish to proceed shopping? (Yes/No): ") #Start of order
    while continue_shopping.lower().startswith('y')  or continue_shopping.lower().startswith('Y'): # == 'yes' or 'y':
        item_added = input("Add an Item: \n")
        if item_added.lower() in str(available_items.keys()).lower():
            print("You've chosen {}".format(item_added)) #Confirmation
            quantity_to_purchase = int(input("How much/many {} would you like? ".format(item_added)))
            if quantity_to_purchase > 0:
                shopping_cart[item_added] = quantity_to_purchase
                # shopping_cart.update({item_added : quantity_to_purchase})
            else:
                print("Please enter a minimum quantity of 1") #Can't pick an item and then enter 0!
        else:
            raise Exception("Item {} is unavailable at this time".format(item_added)) #Error detection
        continue_shopping = input("Do you want to add more items to your cart? (Yes/No): ")

    groc_purch = GroceryPurchased(shopping_cart)
    bill = groc_purch.get_price_for_an_item()
    for itm in bill.items():
        print(itm)
    groc_purch.generate_bill_statement()
