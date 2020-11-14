import unittest
from credential import Credential

class TestCredential(unittest.TestCase):

    """
    Test class that defines test cases for the credential class behaviousrs
    """

    def setUp(self):
        """
        use set up method
        """
        self.new_credential = Credential("instagram","UmutoniRita","rita123")

    def test_init(self):

        '''
        test_init test case to test if the object is initialized properly
        '''
        self.assertEqual(self.new_credential.accountName,"instagram")
        self.assertEqual(self.new_credential.username,"UmutoniRita")
        self.assertEqual(self.new_credential.password,"rita123")

    def test_save_credential(self):
        """
        test save credential to test if the user is saved
        """
        self.new_credential.save_credential()
        self.assertEqual(len(Credential.credential_list),1)

    def tearDown(self):
        """
        tearDown method that does clean up after each test case has run.
        """
        Credential.credential_list = []

    def test_save_multiple_credential(self):
        """
        To test if you can save multiple credential 
        """
        self.new_credential.save_credential()
        test_credential = Credential("gmail","marie","marie123")
        test_credential.save_credential()
        self.assertEqual(len(Credential.credential_list),2)

    def test_delete_credential(self):
        """
        To test if you can delete credential on the list
        """
        self.new_credential.save_credential()
        test_credential = Credential("gmail","marie","marie123") 
        test_credential.save_credential()

        self.new_credential.delete_credential()
        self.assertEqual(len(Credential.credential_list),1)

    def test_find_credential_by_username(self):
        """
        test to check if we can find a credential by username and display information
        """
        

        self.new_credential.save_credential()
        test_credential = Credential("gmail","marie","marie123") 
        test_credential.save_credential()

        found_credential = Credential.find_by_username("marie")

        self.assertEqual(found_credential.accountName,test_credential.accountName)

    def test_credential_exists(self):
        
        """
        test to check if we can return a Boolean  if we cannot find the contact
        """

        self.new_credential.save_credential()
        test_credential = Credential("gmail","marie","marie123")
        test_credential.save_credential()

        credential_exists = Credential.credential_exist("marie")
        self.assertTrue(credential_exists)


if __name__ == '__main__':
    unittest.main()