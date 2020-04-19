class User:

    '''
    Class User, which genereates new users' instances
    '''
    #create an empty list to hold users' data
    passwort_users = []

    def __init__(self, first_name, last_name, password):

        '''
        ___init methof facilitates the definitation of objects' properties.

        Args:
            first_name: New user first_name.
            last_name: New user last_name.
            password: New user password.
        '''
        
        self.first_name = first_name
        self.last_name = last_name
        self.password = password
