import datetime
class Manu:
    item1 = "Sandwich"
    item2 = "Salad"
    item3 = "Soup"
    item4 = "Coffee/Tea"
    def __init__(self):
        print("Our Manu is Given below")
        print("item1 -",self.item1)
        print("item2 -",self.item2)
        print("item3 -",self.item3)
        print("item4 -",self.item4)

class Sandwich(Manu):
    Swprice = 10
    preparation = 10
    def item_1(self):
        SandwichQuantity = int(input("Enter your Sandwich Quantity "))
        if SandwichQuantity>0:
            if SandwichQuantity >=5:
                Order.Sworder(self,self.item1,Sandwich.Swprice, SandwichQuantity)
            else:
                Order.Sdworder(self,self.item1,Sandwich.Swprice,SandwichQuantity)
class CoffeeTea(Manu):
    CTprice = 5
    CTpreparation = 5
    def coffee(self):
        CoffeeQuantity = int(input("How many coffee you want "))
        if CoffeeQuantity>0:
            amount = CoffeeQuantity*self.CTprice
            time = CoffeeQuantity*self.CTpreparation
            Order.Coffeeorder(self,self.item4,CoffeeTea.CTprice,CoffeeQuantity)
    def tea(self):
        TeaQuantity = int(input("How many tea you want "))
        if TeaQuantity>0:
            amount = TeaQuantity*self.CTprice
            time = TeaQuantity*self.CTpreparation
            Order.Teaorder(self, self.item4, CoffeeTea.CTprice, TeaQuantity)
class Soup(Manu):
    Spprice = 6
    Sppreparation = 15
    def item_3(self):
        SoupQuantity = int(input("Enter Soup quantity "))
        if SoupQuantity>0:
            Order.Sporder(self,self.item3, Soup.Spprice, SoupQuantity)
class DSoup(Manu):
    Spprice = 6
    Sppreparation = 15
    def item_3(self):
        DSoupQuantity = int(input("Enter Soup quantity "))
        if DSoupQuantity>0:
            Order.DSporder(self,self.item3, DSoup.Spprice, DSoupQuantity)

class Salad(Manu):
    price_salad = 8
    preparation_salad = 8
    def item_2(self):
        SaladQuantity = int(input("Enter salad quantity "))
        if SaladQuantity>0:
            Order.Slorder(self,self.item2, Salad.price_salad, SaladQuantity)

class DSalad(Manu):
    price_salad = 8
    preparation_salad = 8
    def ditem_2(self):
        DSaladQuantity = int(input("Enter salad quantity "))
        if DSaladQuantity>0:
            Order.DSlorder(self,self.item2, DSalad.price_salad, DSaladQuantity)

class Order(Sandwich,Salad,Soup,CoffeeTea):
    orderlist = []
    itemlist = []
    quantitylist = []
    pricelist = []
    discountlist = []
    timelist = []


    def Sworder(self,itemname,item1,qty1):
        itemname = itemname
        item1 = item1
        qty1 = qty1
        Tbill = item1 * qty1
        Dbill = (Tbill / 100) * 10
        Amount = Tbill - Dbill
        time = qty1 * self.preparation
        self.itemlist.append(itemname)
        self.quantitylist.append(qty1)
        self.pricelist.append(Tbill)
        self.discountlist.append(Amount)
        self.timelist.append(time)
    def Sdworder(self,itemname,item1,qty1):
        itemname = itemname
        item1 = item1
        qty1 = qty1
        Tbill = item1 * qty1
        time = qty1 * self.preparation
        self.itemlist.append(itemname)
        self.quantitylist.append(qty1)
        self.pricelist.append(Tbill)
        self.discountlist.append(Tbill)
        self.timelist.append(time)
    def Sporder(self,itemname,item3,qty3):
        itemname = itemname
        item3 = item3
        qty3 = qty3
        amount = item3 * qty3
        time = qty3 * self.Sppreparation
        self.itemlist.append(itemname)
        self.quantitylist.append(qty3)
        self.pricelist.append(amount)
        self.discountlist.append(amount)
        self.timelist.append(time)
    def DSporder(self,itemname,item3,qty3):
        itemname = itemname
        item3 = item3
        qty3 = qty3
        bill = item3 * qty3
        dbill = ((bill)/100)*20
        amount = bill - dbill
        time = qty3 * self.Sppreparation
        self.itemlist.append(itemname)
        self.quantitylist.append(qty3)
        self.pricelist.append(bill)
        self.discountlist.append((amount))
        self.timelist.append(time)

    def Slorder(self,itemname,item2,qty2):
        itemname = itemname
        item2 = item2
        qty2 = qty2
        amount = item2 * qty2
        time = qty2 * self.preparation_salad
        self.itemlist.append(itemname)
        self.quantitylist.append(qty2)
        self.pricelist.append(amount)
        self.discountlist.append(amount)
        self.timelist.append(time)
    def DSlorder(self,itemname,item2,qty2):
        itemname = itemname
        item2 = item2
        qty2 = qty2
        tbill = item2 * qty2
        dbill = (tbill/100)*10
        amount = tbill - dbill
        time = qty2 * self.preparation_salad
        self.itemlist.append(itemname)
        self.quantitylist.append(qty2)
        self.pricelist.append(tbill)
        self.discountlist.append(amount)
        self.timelist.append(time)

    def Coffeeorder(self,itemname,item2,qty4):
        itemname = itemname
        item2 = item2
        qty4 = qty4
        amount = item2 * qty4
        time = qty4 * CoffeeTea.CTpreparation
        self.itemlist.append(itemname)
        self.quantitylist.append(qty4)
        self.pricelist.append(amount)
        self.discountlist.append(amount)
        self.timelist.append(time)

    def Teaorder(self,itemname,item2,qty4):
        itemname = itemname
        item2 = item2
        qty4 = qty4
        amount = item2 * qty4
        time = qty4 * CoffeeTea.CTpreparation
        self.itemlist.append(itemname)
        self.quantitylist.append(qty4)
        self.pricelist.append(amount)
        self.discountlist.append(amount)
        self.timelist.append(time)

    def Swstore(self):
        self.orderlist.append(self.item1)
        Sandwich.item_1(self)
    def Slstore(self):
        self.orderlist.append(self.item2)
        if "Soup" not in Storage.orderlist:
            Salad.item_2(self)
        else:
            DSalad.ditem_2(self)
    def Spstore(self):
        self.orderlist.append(self.item3)
        if "Sandwich" in Storage.orderlist and "Soup" in Storage.orderlist:
            DSoup.item_3(self)
        else:
            Soup.item_3(self)

    def CTstore(self):
        user = int(input("Press 1 for Coffee\nPress 2 for Tea "))
        if user == 1:
            CoffeeTea.coffee(self)
        elif user == 2:
            CoffeeTea.tea(self)
        else:
            print("Please enter right choice next time")

class Storage(Order):
    def order1(self):
        order = ""
        name = input("Enter your name ")
        while order!="yes":
            print("Which one you want on order")
            user = int(input("Press 1 for Sandwich\nPress 2 for Salad\nPress 3 for soup\nPress 4 for coffee/tea "))
            if user == 1:
                Order.Swstore(self)
            elif user == 2:
                Order.Slstore(self)
            elif user == 3:
                Order.Spstore(self)
            elif user == 4:
                Order.CTstore(self)
            else:
                print("Please select in between 1-4")
            order = input("Have you buy all things press yes for exit no for continue : ")
            Total = 0
            disc = 0
            TotalTime = 0
        print(name, "Thanks for your order")
        print("Items                Qantity                 Price                 DPrice")
        for i , j , k , l , m in zip(self.itemlist,self.quantitylist,self.pricelist,self.discountlist,self.timelist):
            print(i, "             ", j, "                    ", k, "                    ", l)
            Total = Total + k
            TotalTime = TotalTime + m
            disc = disc + (k-l)
            Payable = Total-disc
        print("Tax =             0")
        print("Total =           ", Total)
        print("Discount =       ",disc)
        print("Payable =       ", Payable)
        print((datetime.datetime.today(), "Your order will be ready in", TotalTime, "minutes"))

object = Storage()
object.order1()
