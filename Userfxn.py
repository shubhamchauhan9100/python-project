import random
from adminfxn import Admin
class User:
    user_profile ={}
    order_history={}
    def Register(self):
        userid=random.randint(1,99)
        name=input("enter name\t")
        phoneno=int(input("enter phn no.\t"))
        email=input("enter email\t")
        address=input("enter address\t")
        password=input("enter password\t")
        print("congratulation on registering ,kindly login to proceed further")
        User.user_profile[userid]={
            "name":name,
            "userid":userid,
            "phoneno":phoneno,
            "email":email,
            "address":address,
            "password":password}
        print("your user ID\t",userid,"   & your password is\t", password)

    def login_password(self,userid,password):
        if User.user_profile[userid]["password"]==password:
            print("you login in successfully")
            return False
        else:
            return True

    def update_profile(self):
        ID = int(input("Enter the User ID which you want to edit: "))
        a = input("Enter the item User Name : ")
        b = int(input("Enter the User Phone Number : "))
        c = input("Enter the User Address : ")
        d = input("Enter the User Email ID : ")
        e = input("Enter new Password : ")
        User.user_profile[ID]["name"] = a
        User.user_profile[ID]["phoneno"] = b
        User.user_profile[ID]["address"] = c
        User.user_profile[ID]["email"] = d
        User.user_profile[ID]["password"] = e

    def user_menu(self):
        print("*HERE IS THE All Item of FoodApp*",'\n')
        for i in Admin.All_Item:
            if Admin.All_Item[i]["Stock"]>0:
                print("Item ID: ",Admin.All_Item[i]["ItemID"])
                print("Item Name: ",Admin.All_Item[i]["ItemName"])
                print("Price: ",Admin.All_Item[i]["Price"],"INR")
                print("Quantity: ",Admin.All_Item[i]["Quantity"],"Piece \n")

    def place_order(self):
        temp_ord_dic={}
        print("What you want to order")
        print(self.user_menu())
        user_choice = int(input("If you want to order then enter '1' for YES '2' for NO \n"))
        if user_choice == 1:
            ID = int(input("Enter the User ID which you want to order: "))
            n=list(input("Enter list of items, you want to Order : "))
            order_id=random.randint(1,99)
            x=0
            for i in n:
                x += Admin.All_Item[i]["Price"] * (100-(Admin.All_Item[i]["Discount"]))
                temp_ord_dic[i]= {
                    "Item Name": Admin.All_Item[i]["ItemName"],
                    "Price": Admin.All_Item[i]["Price"],
                }
                User.order_history[ID][order_id]= temp_ord_dic
                    
            print(f"It costs you {x}INR in total")
            print("You're all set for this order")
            
            again_ask = input("Are you want to order this Enter YES or NO \n")
            if again_ask == "YES":
                print("You're order is successfully placed")
                print("your order ID is:",order_id)

            elif again_ask == "NO":
                print("This Order is cancelled!! You can look once more")
            else:
                print("Invalid choice")
        elif user_choice == 2:
            print("You select 2 option so we cancelled this")
        else:
            print("Enter the invalid choice")

    def view_order_history(self):
        ID = int(input("Enter the User ID which you want to edit: "))
        print("The order history : " + str(User.order_history[ID]))
