import pyperclip
import string
import random

class User:

    '''
    Class User, which generates new users' instances
    '''
    #Create an empty list to hold users' data
    passwort_users = []

    def __init__(self, first_name, last_name, password):

        '''
        __init__ method facilitates the definitation of objects' properties.

        Args:
            first_name: New user first_name.
            last_name: New user last_name.
            password: New user password.
        '''
        
        self.first_name = first_name
        self.last_name = last_name
        self.password = password
    
    #Save a single user
    def save_user(self):

        '''
        save_user() saves user objects in the passwort_users list
        '''
        User.passwort_users.append(self)

    #Check if user exists
    @classmethod
    def user_exists(cls,first_name):

        '''
        user_exists() uses a user's first name to determine if they exist

        Args:
            first_name: name to search

        Returns:
            Boolean: true or false if the user exists or doesn't exist respectively
        '''
        for user in cls.passwort_users:
            if user.first_name == first_name:
                return True
        return False


class Credentials:

    '''
    Class Credentials generates new credentials objects
    '''

    #Empty credentials' list
    referenzen_list = []

    #Initialize
    def __init__(self, first_name, username, site_name, password):

        '''
        __init__ method facilitates the definitation of objects' properties.

        Args:
            first_name: New user first_name.
            username: New user username.
            site_name: New site name.
            password: New site password.
        '''
        
        self.first_name = first_name
        self.username = username
        self.site_name = site_name
        self.password = password

    #Authenticate user
    @classmethod
    def authenticate_user(cls,first_name,password):
        '''
        authentic_user() checks if user first name and password match
        '''

        #Define current user
        current_user = ''
        
        for user in User.passwort_users:
            if user.first_name == first_name and user.password == password:
                current_user = user.first_name
        return current_user 

    #Save a single credential
    def save_credentials(self):

        '''
        save_credentials() adds a new credential to the referenzen list
        '''

        Credentials.referenzen_list.append(self)

    #Display all credentials
    @classmethod
    def display_credentials(cls):

        '''
        Method returns a list of all saved credentials
        '''

        return cls.referenzen_list
    
    #Find credential using site name
    @classmethod
    def find_by_site(cls,site_name):

        '''
        method finds saved credentials using the provided site name

        Args:
            site_name: name to search for 

        Returns:
            credentials associated with the provided site name 
        '''

        for credential in cls.referenzen_list:
            if credential.site_name == site_name:
                return credential

    def delete_credential(self):

        '''
        delete_credential() deletes saved credential stored in the referenzen list
        '''

        Credentials.referenzen_list.remove(self)

    #copy password
    @classmethod
    def copy_password(cls,site_name):
        credential_found = Credentials.find_by_site(site_name)
        copied_password = pyperclip.copy(credential_found.password)
        return copied_password 

    


          




