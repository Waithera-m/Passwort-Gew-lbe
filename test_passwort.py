import unittest
import pyperclip
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

    def tearDown(self):
            '''
            tearDown method that does clean up after each test case has run.
            '''
            User.passwort_users = []

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
        self.new_credential = Credentials("Mary", "Njihia", "reddit", "hgnkf2542")

    def tearDown(self):
            '''
            tearDown method that does clean up after each test case has run.
            '''
            Credentials.referenzen_list = []


    #Authenticate user
    def test_authenticate_user(self):
        
        '''
        the test case checks if the password a user has entered corresponds with the one that has been saved.

        Args:
            first_name: user's first_name
            password: user's password

        Returns:            
            User: current user, outcome determined by results of the logical operator
        '''
        self.new_user = User("Mary", "Njihia", "hgnkf254")
        self.new_user.save_user()
        user_zwei = User("Jane", "Doe", "pass100")
        user_zwei.save_user()
        
        for user in User.passwort_users:
            if user.first_name == user_zwei.first_name and user.password == user_zwei.password:
                current_user = user.first_name

        self.assertEqual(current_user, Credentials.authenticate_user(user_zwei.first_name, user_zwei.password))
        return current_user

    #Check if instance initializes properly 
    def test_init(self):
        

        '''
        test_init test case checks if object is initatilized properly
        '''

        self.assertEqual(self.new_credential.first_name, "Mary")
        self.assertEqual(self.new_credential.username, "Njihia")
        self.assertEqual(self.new_credential.site_name, "reddit")
        self.assertEqual(self.new_credential.password, "hgnkf2542")
    
    #Test if a credential is saved
    def test__save_credentials(self):

        '''
        test case checks if new credentials are saved to the referenzen_list
        '''

        self.new_credential.save_credentials()
        self.assertEqual(len(Credentials.referenzen_list), 1)

    #Test if multiple credentials are saved
    def test_save_multiple_credentials(self):

        '''
        test case checks if it is possible to save multiple credentials in the referenzen list
        '''

        self.new_credential.save_credentials()
        test_credential = Credentials("Mary", "Peaches", "twitter", "peaches123")
        test_credential.save_credentials()
        self.assertEqual(len(Credentials.referenzen_list),2)

    #Test: display credentials
    def test_display_credentials(self):

        '''
        test case returns a list of all saved credentials
        '''

        self.assertEqual(Credentials.display_credentials() ,Credentials.referenzen_list)

    #Test find password by site name
    def test_find_by_site(self):

        '''
        test to find out if user can find credentials using site name
        '''

        self.new_credential.save_credentials()
        test_credential = Credentials("Jane", "Eyre", "facebook", "char257")
        test_credential.save_credentials()

        found_credential = Credentials.find_by_site("facebook")
        
        self.assertEqual(found_credential.password, test_credential.password)

    #Delete credential
    def test_delete_credential(self):

        '''
        test case to determine if it is possible to remove a credential from the credential list
        '''

        self.new_credential.save_credentials()
        test_credential = Credentials("Jane", "Eyre", "facebook", "char257")
        test_credential.save_credentials()

        self.new_credential.delete_credential()
        self.assertEqual(len(Credentials.referenzen_list),1)

    #Test copy credential
    def test_copy_password(self):

        '''
        test to confirm that it is possible to copy to the machine's clipboard
        '''
        self.new_credential.save_credentials()
        Credentials.copy_password("reddit")

        self.assertEqual(self.new_credential.password,pyperclip.paste())
        

    
    



    

              
        

        
        


    



    


if __name__ == '__main__':
    unittest.main()