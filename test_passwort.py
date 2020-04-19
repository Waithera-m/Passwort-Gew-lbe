import unittest
from passwort import User, Credentials

class TestUser(unittest.TestCase):

    '''
    subclass inherits from TestCase and defines individual test units for the User class behavior

    Args:
        unittest.Testcase: TestCase class to facilitate the creation of test units
    '''

    def setUp(self):

        '''
        setUp() method defines the instructions that will be excuted before each test method
        '''
        self.new_user = User("Mary", "Njihia", "hgnkf254")

    #Test if it possible to create a new user
    def test_init(self):
        

        '''
        test_init test case checks if object is initatilized properly
        '''

        self.assertEqual(self.new_user.first_name, "Mary")
        self.assertEqual(self.new_user.last_name, "Njihia")
        self.assertEqual(self.new_user.password, "hgnkf254")

    #Test saving a single user
    def test_save_user(self):

        '''
        test_save_user test case checks if new user's information is saved to the passwort_users list
        '''
        self.new_user.save_user()
        self.assertEqual(len(User.passwort_users), 1)

    #Check is user exists 
    def test_user_exists(self):

        '''
        test if a user's account exists, return a boolean value
        '''
        self.new_user.save_user()
        user_exists = User.user_exists("Mary")
        self.assertTrue(user_exists)
    

class TestCredentials (unittest.TestCase):

    '''
    subclass inherits from TestCase and defines individual test units for the Credentials class behavior

    Args:
        unittest.Testcase: TestCase class to facilitate the creation of test units
    '''

    def setUp(self):

        '''
        SetUp() method defines the instructions that will be excuted before each test method
        '''
        self.new_user = User("Mary", "Njihia", "hgnkf254")

    



    


if __name__ == '__main__':
    unittest.main()