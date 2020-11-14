class Credential:
    """
    class that generates accountName,username and password of credentials 
    """
    credential_list = [] 

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

