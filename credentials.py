#!/usr/bin/env python3.6
from user import User
from user import Account

def create_user(firstname,lastname,username,password):
    new_user = User(firstname,lastname,username,password)
    return new_user

def save_user(user):
    user.save_user()

def delete_user(user):
    user.delete_user()

def find_user(username):
    return User.find_by_username(username)

def find_password(userpassword):
    return User.find_by_userpassword(userpassword)

def display_user():
    return User.display_userInfo()



def create_account(accountname,accountusername,accountpassword):
    new_account = Account(accountname,accountusername,accountpassword)
    return new_account

def save_account(user):
    user.save_account()

def delete_account(user):
    user.delete_account()

def display_account_credentials():
    return Account.display_accounts()

def find_account_credentials(accountname):
    return Account.find_by_accountName(accountname)





def main():

    print("Welcome to Password Locker. What is your name?")
    name = input()
    print(f"Hello {name}!To start off please choose one of the options below:")
    print('\n')

    while True:
        print("this short code helps to signup: na - SignUp")
        user_choice = input().lower()

        if user_choice == "na":
            print("Create an account")
            print("-"*7)
            print("Enter First Name:")

            firstname = input()

            print("Enter Last Name:")
            lastname = input()

            print("Enter Username:")
            username = input()

            print("Enter password")
            password = input()

            save_user(create_user(firstname,lastname,username,password)) 
            print('\n')
            print(f"New user {firstname} {lastname} has been created.You can now proceed to login with your credentials.")
            print('\n')


        elif user_choice == "lg":
            print("Enter your Username:")
            login_userName = input()

            print("Enter your password:")
            login_password = input()

            if find_user(login_userName) and find_password(login_password):
                print('\n')
                print("Welcome!To continue please choose any of the options below:")
                print("-"*60)

                print("nw - Add New Account, da - Display Accounts, vw -View Account Details, dlt - Delete Account Detaiils")

                account_choice = input().lower()

                if account_choice == "nw":
                    print("Enter Account Name:")
                    accountname = input()

                    print("Enter Account Username:")
                    accountusername = input()

                    print("Enter Account Password:") 
                    accountpassword = input()

                    save_account(create_account(accountname,accountusername,accountpassword)) 
                    print(f"Account Name:{accountname}, Account Username:{accountusername}, Account Password:{accountpassword}")


                elif account_choice == "da":
                    if display_account_credentials():
                        print("Here is a list of all your accounts: ")
                        print('\n')

                        for account in display_account_credentials():
                            print(f"Account Name:{account.account_name}")

                    else:
                        print("invalid choice")


                elif account_choice == "vw":
                    print("Enter an Account Name:")
                    account_choiceName = input()

                    if display_account_credentials():
                        account_choiceName = find_account_credentials(account_choiceName)
                        print(f"Account Username:{account_choiceName.account_userName}   Password:{account_choiceName.account_password}")

                    else:
                        print(f"{account_choiceName} does not exist")



                elif account_choice == "dlt":
                    print("Enter Account Name:")
                    delete_acc = input()

                    if delete_account(delete_acc):
                        return delete_account(delete_acc)

                    else:
                        print(f"{delete_acc} does not exist")


            else:
                print("Incorrect username or password.Please try again.")
                print('\n')


        else:
            print("Incorrect Option.Please choose from the ones listed")
            print('\n')



if __name__ == '__main__':
    main()