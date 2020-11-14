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

    print(f"Hello, {user_name} what wouldyou like to do?")
    print("\n")

if __name__ == '__main__':
    password_locker()