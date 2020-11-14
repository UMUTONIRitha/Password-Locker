#!/usr/bin/env python3.6
import pyperclip

from user import User


class Credential:
    """
    class that generates accountName,username and password of credentials 
    """
    credential_list = [] 

    @classmethod
    def verify_user(cls,username,password):
        """
        method to verify whether the user is on the list of the user
        """
        current_user = ""
        for user in User.user_list:
            if(user.username == username and user.password == password):
                current_user == user.username
        return current_user


    def __init__(self,accountName,username,password):

        """
        use __init__ method and define properties 
        """
        self.accountName = accountName
        self.username = username
        self.password = password

    def save_credential(self):

        """
        save_cridential method to saves credential object into credential list
        """
        Credential.credential_list.append(self)

    def delete_credential(self):
        """
        delete credential method to delete credential object on the list
        """
      
        Credential.credential_list.remove(self)

    @classmethod
    def find_by_username(cls,username):
        """
        Method that takes in username and returns a credential that matches that username.
        """
      

        for name in cls.credential_list:
            if name.username == username:
                return name

    @classmethod
    def copy_password(cls,username):
        credential_found = Credential.find_by_username(username)
        pyperclip.copy(credential_found.password)

    @classmethod 
    def credential_exist(cls,username):
        """
        Method that checks if a credential exists from the credential list.
        """


        for name in cls.credential_list:

            if name.username == username:

                return True

        return False

    @classmethod
    def display_credential(cls):
        """
        display credential method to display list of credential
        """
        return cls.credential_list


