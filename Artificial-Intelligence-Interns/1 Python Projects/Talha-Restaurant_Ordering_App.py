import datetime

class Menu:
    item1 = "Sandwich"
    item2 = "Salad   "
    item3 = "Soup   "
    item4 = "Coffee/Tea"

    def __init__(self):
        print("Our Menu is Given below")
        print("item1:", self.item1)
        print("item2:", self.item2)
        print("item3:", self.item3)
        print("item4:", self.item4)

class Sandwich(Menu):
    price = 10
    preparationTime = 10

    def item_1(self):
        quantity = int(input("How many Sandwiches do you want: "))
        if quantity > 0:
            if quantity >= 5:
                print(Order.DiscSandwichOrder(self, self.item1, Sandwich.price, quantity))
            else:
                print(Order.SandwichOrder(self, self.item1, Sandwich.price, quantity))

class CoffeeTea(Menu):
    price = 5
    preparationTime = 5

    def item_4(self):
        quantity = int(input("How many Coffee/Tea do you want: "))
        if quantity > 0:
            print(Order.CoffeeTeaOrder(self, self.item4, CoffeeTea.price, quantity))

class Salad(Menu):
    price = 5
    preparationTime = 15

    def item_2(self):
        quantity = int(input("How many Salads do you want: "))
        if quantity > 0:
            if "Soup" in Order.order_list:
                print(Order.DiscSaladorder(self, self.item2, Salad.price, quantity))
            else:
                print(Order.SaladOrder(self, self.item2, Salad.price, quantity))

class Soup(Menu):
    price = 6
    preparationTime = 15

    def item_3(self):
        quantity = int(input("How many Soups do you want: "))
        if quantity > 0:
            if "Sandwich" in Order.order_list and "Salad" in Order.order_list:
                print(Order.DiscSoupOrder(self, self.item3, Soup.price, quantity))
            else:
                print(Order.SoupOrder(self, self.item3, Soup.price, quantity))

class Order(Sandwich, CoffeeTea, Salad, Soup):
    order_list = []
    itemlist = []
    quantitylist = []
    pricelist = []
    discountlist = []
    timelist = []

    def DiscSandwichOrder(self, itemname, price, quantity):
        itemname = itemname
        price = price
        quantity = quantity
        TotalBill = price * quantity
        Discount = (TotalBill / 100) * 10
        Amount = TotalBill - Discount
        time = Sandwich.preparationTime * quantity
        self.order_list.append(itemname)
        self.itemlist.append(itemname)
        self.quantitylist.append(quantity)
        self.pricelist.append(TotalBill)
        self.discountlist.append(Discount)
        self.timelist.append(time)

    def SandwichOrder(self, itemname, price, quantity):
        itemname= itemname
        price = price
        quantity = quantity
        TotalBill = price * quantity
        time = Sandwich.preparationTime * quantity
        Discount = 0
        self.order_list.append(itemname)
        self.itemlist.append(itemname)
        self.quantitylist.append(quantity)
        self.pricelist.append(TotalBill)
        self.discountlist.append(Discount)
        self.timelist.append(time)
    def CoffeeTeaOrder(self, itemname, price, quantity):
        itemname= itemname
        price = price
        quantity = quantity
        TotalBill = price * quantity
        time = CoffeeTea.preparationTime * quantity
        Discount = 0
        self.order_list.append(itemname)
        self.itemlist.append(itemname)
        self.quantitylist.append(quantity)
        self.pricelist.append(TotalBill)
        self.discountlist.append(Discount)
        self.timelist.append(time)
        
    def SaladOrder(self, itemname, price, quantity):
        itemname= itemname
        price = price 
        quantity = quantity
        TotalBill = price * quantity
        time = Salad.preparationTime * quantity
        Discount = 0
        self.order_list.append(itemname)
        self.itemlist.append(itemname)
        self.quantitylist.append(quantity)
        self.pricelist.append(TotalBill)
        self.discountlist.append(Discount)
        self.timelist.append(time)
    
    def DiscSaladorder(self,itemname, price, quantity ):
        itemname= itemname
        price = price 
        quantity = quantity
        TotalBill = price * quantity
        time = Salad.preparationTime * quantity
        Discount = (TotalBill / 100) * 10
        self.order_list.append(itemname)
        self.itemlist.append(itemname)
        self.quantitylist.append(quantity)
        self.pricelist.append(TotalBill)
        self.discountlist.append(Discount)
        self.timelist.append(time)
        
    def SoupOrder(self,itemname,  price, quantity):
        itemname= itemname
        price = price 
        quantity = quantity
        TotalBill = price * quantity
        time = Salad.preparationTime * quantity
        Discount = 0
        self.order_list.append(itemname)
        self.itemlist.append(itemname)
        self.quantitylist.append(quantity)
        self.pricelist.append(TotalBill)
        self.discountlist.append(Discount)
        self.timelist.append(time)
        
    def DiscSoupOrder(self,itemname,  price, quantity):
        itemname= itemname
        price = price 
        quantity = quantity
        TotalBill = price * quantity
        time = Salad.preparationTime * quantity
        Discount = (TotalBill / 100) * 20
        self.order_list.append(itemname)
        self.itemlist.append(itemname)
        self.quantitylist.append(quantity)
        self.pricelist.append(TotalBill)
        self.discountlist.append(Discount)
        self.timelist.append(time)
    
class Choice(Order):
    def Choicefunction(self):
        item_name = ""
        User_input = "" 
        while User_input != "Done":
            item_name = int(input("Press 1 for Sandwich, 2 for Salad, 3 for Soup, and 4 for Coffee/Tea: "))
            if item_name == 1:
                Sandwich.item_1(self)
            elif item_name == 2:
                Salad.item_2(self)
            elif item_name == 3:
                Soup.item_3(self)
            elif item_name == 4:
                CoffeeTea.item_4(self)
            else:
                print("Please enter a number between 1 and 4.")
            User_input = input("If you press 'Done', exit; otherwise, press any other key to continue: ")

        name = input("Enter your name: ")
        print(f"{name}, thanks for your order")
        print("Items\t\t\tQuantity\t\t\tPrice\t\t\tDiscount")

        for item, quantity, price, discount, time in zip(self.itemlist, self.quantitylist, self.pricelist, self.discountlist, self.timelist):                                                        
            print(item, "\t\t\t", quantity, "\t\t\t", price, "\t\t\t", discount)
        TotalBill = sum(self.pricelist) - sum(self.discountlist)
        TotalTime = sum(self.timelist)
        print("Tax = 0")
        print("Total Bill =", TotalBill)
        print(datetime.datetime.now(), "Your order will be ready in", TotalTime, "minutes")
choice = Choice()
choice.Choicefunction()


