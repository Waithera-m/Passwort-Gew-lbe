#!/usr/bin/env python3.8
import pyperclip
import random
from passwort import User, Credentials

def create_user(fname,username,password):

    '''
    method to create a new user
    '''
    new_user = User(fname,username,password)
    return new_user

def add_user(user):

    '''
    method to save a user
    '''
    user.save_user()

def check_user(user):

    '''
    method to check if user exists
    '''
    user.user_exists()

def create_credential(un_name,username,site,password):

    '''
    method to create new credentials
    '''
    new_credential = Credentials(un_name,username,site,password)
    return new_credential

def authenticate(first_name,password):

    '''
    method to check match between user and provided password
    '''
    return Credentials.authenticate_user(first_name,password)

def save_credential(credential):

    '''
    method to save credentials
    '''
    credential.save_credentials()

def display_credentials():

    '''
    method to display all saved credentials
    '''
    return Credentials.display_credentials()

def get_credential(site_name):

    '''
    method to look for credential using site_name
    '''
    return Credentials.find_by_site(site_name)

def remove_credential(credential):

    '''
    method to delete a credential
    '''
    credential.delete_credential()

def copy_password(site_name):

    '''
    method to copy credential to machine clipboard
    '''
    return Credentials.copy_password(site_name)


    
    
    

def main():
    print("Hello and welcome to Passwort-Gew-lbem, your personal password manager.")
    print('\n')
    print("What is your name?")
    print("-"*70)
    user_name = input()
    print('\n')
    print(f"Hi {user_name}. What would you like to do?")
    print('\n')
    while True:
        print("Use any of the following shortcodes to enter your commands: \n au - create user \n su - save user \n uf - find user \n ac - create credential \n lo - login \n dc - display credentials \n fc - find credential \n rc - delete credential \n cc - copy credential \n ex - exit")
        print('\n')
        short_code = input().lower()

        print("-"*70)
        if short_code == "au":
            print("New User")
            print("-"*10)
            print("First Name...")
            fname = input()
            print("Username...")
            username = input()
            print("Password...")
            password = input()

            add_user(create_user(fname, username,password))
            print('\n')
            print(f"New user {fname} created")
            print('\n')
            print("-"*70)

        elif short_code == "ac":
            print("Please enter your credentials:")
            un_name =  input("Please enter your first name: ")
            username = input("please enter your username: ")
            site = input("Please enter the account's name: ")
            while True:
                print('\n')
                print("Select: \n es - to enter an existing pasword \n gp - to generate a new password")
                create_choice = input("Please indicate if you would like to enter an existing or generate a new password: ").lower().strip()
                if create_choice == "es":
                    print("Please enter your password: ")
                    password = input()
                    break
                elif create_choice == "gp":
                    string_characters = "abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*?"
                    password = "".join(random.sample(string_characters,10))
                    
                    break
                    
                else:
                    print("Oops, please try again")

            save_credential(create_credential(un_name,username, site, password))
            print('\n')
            print(f"Credential {username} for {site} with password: {password} created")
            print('\n')

        elif short_code == "uf":
            print("Please enter the site name you want to search for:  ") 
            search_site = input()
            print("Please enter the first name used to save the crdential: ")
            first_name = input()
            if check_user(first_name):
                search_credential = get_credential(search_site)
                print(f"{search_credential.site}") 
                print(f"Username: {search_credential.username} Password: {search_credential.password}")
            else:
                print("I cannot find that credential")

        elif short_code == "dc":
            if display_credentials():
                print("Here are your saved credentials")
                print('\n')
                for credential in display_credentials():
                    print(f"{credential.username}...{credential.site}...{credential.password}")
                print('')
            else:
                print("There are no sve credentials")
                print("Tip: save some credentials and then reenter the command :D")

        elif short_code == "rc":
            if remove_credential(credential):
                print("Enter the name, username, site, and password of the credential to delete: ")
                credential = input()
                remove_credential(credential)

        elif short_code == "cc":
            print("Please enter the site name of the credential password to copy: ")
            site_entered = input()
            copy_password(site_entered)

        elif short_code == "ex":
            print("Bye, bis bald...")
            break

        else:
            print("I did not catch that. Please use the shortcodes provided. Thank you")
        
if __name__ == '__main__':
    main()






                  