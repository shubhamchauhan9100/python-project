from Userfxn import User
from adminfxn import Admin

def login_choice():
    choice=int(input("select one of the following options:\n1)Sign up\n2)Login IN \n3)Close the APP\n"))
    return choice

def sign_up_choice():
    choice=int(input("Do you want to sign in as:\n1)User\n2)return to previous page:\n"))
    return choice

def user_option_page():
    choice=int(input("Do you want to:\n1)order\n2)update profile\n3)order history\n4)login again\n"))
    return choice

def admin_option_page():
    choice=int(input("Do you want to:\n1)add food item\n2)stock \n3)edit food item\n4)remove food item\n5)return to previous page:\n"))
    return choice

userfunction_obj=User()

first_page_loop=True
while first_page_loop:
    choice=login_choice()
    if choice==1:
        sign_up_as=sign_up_choice()
        if sign_up_as==1:
            userfunction_obj.Register()
            choice=2
        elif sign_up_as==2:
            continue
    elif choice==2:
        login_as=int(input("Do you want to sign in as:\n1)User\n2)admin\n3)return to previous page:\n"))
        if login_as==1:
            while True:
                user_ID,password=input("Enter user ID & password to login\n").split()
                try:
                    userfunction_obj.login_password(int(user_ID),password)
                except:
                    print("wrong user_ID or password")
                    continue
                user_option=user_option_page()
                if user_option==1:
                    userfunction_obj.place_order()
                    break
                elif user_option==2:
                    userfunction_obj.update_profile()
                    break
                elif user_option==3:
                    userfunction_obj.view_order_history()
                    break
                elif user_option==4:
                    continue
        elif login_as==2:
            while True:
                admin_option=admin_option_page()
                if admin_option==1:
                    Admin.add_new_item()
                    break
                elif admin_option==2:
                    Admin.show_stock()
                    break
                elif admin_option==3:
                    Admin.edit_food_item()
                    break
                elif admin_option==4:
                    Admin.remove_item()
                    break
                elif admin_option==5:
                    continue
        elif login_as==3:
            continue
    elif choice==3:
        first_page_loop=False