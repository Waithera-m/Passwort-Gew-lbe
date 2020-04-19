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
    
    #Intialize
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


