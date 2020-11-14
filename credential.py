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
        save_cridential method to saves users object into user list
        """
        Credential.credential_list.append(self)
