print("welcome to Alishba's bakery ")
print("bakery menu ")
menu = {
    "bread"     :  5.99,
    "cookies"   :  1.99,
    "pasteries" :  2.0,
    "cakes"     :  6.00
}

order = []

print("1. add item to order ")
print("2. view order ")
print("3. calculate total ")
print("4. quit ")

choice = int(input("enter your choice "))

if choice == 1:
    item = input("enter the item you want to order ")
    if item in menu:
        order.append(item)
        print(item , "add to your order ")
        check_order = int(input("Press 2 If you want to see your order then "))
        if check_order == 2:
            print("your order",order)
        else:
            print("Try again")    
        check_bill = int(input("Press 3 If you want to check bill of your order"))
        if check_bill == 3:
            bill = menu[item]
            print(bill)
        else:
            print("Try again")        
    else:
        print(item , "not found in menu")
    
elif choice == 2:
    print("You have not ordered yet")

elif choice == 3:
    print("You have not not ordered yet so your bill is 0")

elif choice == 4:
    print("thankyou for choosing us")
    print("GOOD BYE")

else:
    print("invalid try, please choose something else")