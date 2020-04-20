#!/usr/bin/env python3.8
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

def show_credentials():

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

def to_clipboard(site_name):

    '''
    method to copy credential to machine clipboard
    '''
    return Credentials.copy_password(site_name)

def create_password(sname):

    '''
    method to generate new password
    '''
    sname.generate_new_password()

def main():






