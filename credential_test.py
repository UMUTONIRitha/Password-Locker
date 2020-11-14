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

if __name__ == '__main__':
    unittest.main()