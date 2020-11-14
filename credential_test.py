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
        to save multiple credential 
        """
        self.new_credential.save_credential()
        test_credential = Credential("gmail","marie","marie123")
        test_credential.save_credential()
        self.assertEqual(len(Credential.credential_list),2)

if __name__ == '__main__':
    unittest.main()