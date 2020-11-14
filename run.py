#!/usr/bin/env python3.6
from user import User
from credential import Credential
import random
import string
import sys

def create_users(username,password):
    """
    function to create a new user
    """
    new_user = User (username,password)
    return new_user

def save_users(user):
    """
    Function to save user
    """
    user.save_user()

def display_users(user):
    """
    Function to display saved user
    """
    user.display_user()

def login_user(username,password):
    """
    Function that checks whether a user exist and then login 
    """
    check_user = Credential.verify_user(username,password)
    return check_user

def delete_users(user):
    """
    Function to delete a user
    """
    user.delete_user()

def create_credential(accountName,username,password):
    """
    function to create a new credential
    """
    new_credential = Credential (accountName,username,password)
    return new_credential

def save_credentials(credential):
    """
    Function to save credential
    """
    credential.save_credential()

def passwords_generate(size = 8, characters=string.ascii_letters + string.digits + string.punctuation):
    """
    Generate random password of string letters,digits and ponctuation
    """
    return''.join(random.choice(characters)for i in range(size))

def display_credentials(credential):
    """
    Function to display saved credential
    """
    return Credential.display_credential()

def delete_credentials(credential):
    """
    Function to delete a credential
    """
    credential.delete_credential()

def find_credentials(username):
    """
    function that finds in username and returns a credential that matches that username
    """
    return Credential.find_by_username(username)

def exist_credentials(username):
    """
    Function that checks if a credential exists from the credential list and return true or false.
    """
    return Credential.credential_exist(username)

def copy_passwords(username):
    """
    function that copy password
    """
    return Credential.copy_password(username)

def password_locker():
    print("Welcome to Password Locker\n ")
    user_name = input()

    print(f"Hello, {user_name} what would you like to do? \n CA --- Create new account \n HA ---- Have account\n ")
    short_code = input("").lower().strip()
    if short_code == "ca":
        print("Sign Up")
        print('*' * 30)
        username = input("User_name: ")

        while True:
            print("TP - To type your own Password:\n GP - Generate random Password")
            password_choice = input().lower().trip()
            if password_choice == 'tp':
                password = input("Enter Password\n")
                break
            elif password_choice == 'gp':
                password = passwords_generate()
                break
            else:
                print("Invalid password please try again")

        save_users(create_users(username,password))
        print("*" * 50)
        print(f"Hello {username},Your account has been created succcessful! Your password is : {password}")
        print("*" * 50)
    elif short_code == "ha":
        print("*" * 35)
        print("Enter your User name and your Password to log in:")
        print("*" * 35)
        username = input("User name: ")
        password = input("password: ")
        login = login_user(username,password)
        if login_user == login:
            print(f"Hello {username}. Welcome To Password Locker Functions")
            print("\n")

    while True:
        print("User these short codes:\n CC - Create a new Credential \n DC - Display Credential \n FC - Find a Credential \n GP - Generate a random Password \n DC - Delete Credential \n EX - Exit the application\n")
        short_code = input().lower().strip()
        if short_code == "cc":
            print("Create New Credential")
            print("." * 20)
            print("Account name  ....")
            account = input().lower()
            print("Your Account username")
            username = input()
            while True:
                print("TP - Type your own password if you already have an account:\n GP - Generate random Password")
                password_choice = input().lower().strip()
                if password_choice == "tp":
                    password = input("Enter your own Password\n")
                    break
                elif password_choice == 'gp':
                    password = passwords_generate()
                    break
                else:
                    print("Invalid password please try again")
            save_credentials(create_credential(accountName,username,password))
            print("\n")
            print(f"Account Credential for: {accountName} - username: {username} - password:{password} created successfully")
            print("\n")

        elif short_code == "dc":
            if display_credentials():
                print("Here there is list of your acoounts: ")

                print("*" * 20)
                print("_" * 20)
                for name in display_credentials():
                    print(f"Accountname:{name.accountName} \n User Name:{username}\n Password:{password}")
                    print("_" * 20)
                print("*" * 20)
            else:
                print("You don't have any credentials save yet..........")
                print("\n")
        elif short_code == "dc":
            print("Enter the account name of the Credentials you want to delete")
            search_name = input().lower()
            if find_credentials(search_name):
                search_credential = find_credentials(search_name)
                print("_" * 35)
                search_credential.delete_credential()
                print("\n")
                print(f"Your stored credentials for : {search_credential.username} successful deleted!")
                print("\n")
            else:
                print("that credential you want to delete does not exist in this app yet")
        elif short_code == "gp":
            passsword = passwords_generate()
            print(f" {password} has been generated successful. you can proced to use it to your account name")

        elif short_code == "ex":
            print("thanks for using password locks, see you next time!")
            break
        else:
            print("please enter valid input!")
            



if __name__ == '__main__':
    password_locker()