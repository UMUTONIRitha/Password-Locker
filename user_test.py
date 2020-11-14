import unittest
from user import User

class TestUser(unittest.TestCase):

    """
    Test class that defines test cases for the user class behaviousrs
    """

    def setUp(self):
        """
        use set up method
        """
        self.new_user = User("UmutoniRita","rita123")

    def test_init(self):

        '''
        test_init test case to test if the object is initialized properly
        '''
        self.assertEqual(self.new_user.username,"UmutoniRita")
        self.assertEqual(self.new_user.password,"rita123")

if __name__ == '__main__':
    unittest.main()
