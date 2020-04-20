# Passwort-Gew-lbe
#### Passwort-Gew-lbe is a simple Python password locker, April 20, 2020
#### By Waithera-M
## Description
Passwort-Gew-lbe is a simple Python application that allows a user to create an account, add multiple site credentials, and view and delete these credentials
## Setup/Installation Requirements
### Prerequsites
To run the application a user needs to install:
* Python 3.8.2, other Python 3 versions are also appropriate
* Pip - Python's package installer, please note that the installer is usually preinstalled in Python 3.4 and later versions
* Pyperclip
* xsel -the mechanism ensures the smooth functioning of the pyperclip module 
### Set-Up a Local Project
* Clone the repository using the git clone command
* To run the app on your terminal, run chmod +x password_locker.py and ./run.py respectively
## Known Bugs
* The execution of the copy command method is flawed
## Behavior Driven Development(BDD)
|Behavior        |Input                          |Output                                 |
|----------------|-------------------------------|---------------------------------------|
|Run run.py      |User enters name when prompted   |User sees a list of possible commands  |
|User types au   |User enters name, username, and password| App notifies the user that a new account has been created|
|User types ac |User enters credentials's details and opts to generate or manually add a password| program notifies user that a credential has been created|
|User types dc  |No expected input |User sees a list of saved credentials and if they are none s/he or they are notified that there are no saved crdentials|
|User types rc |User indicates the index of the credential to be deleted|The indicated credential is deleted|
|User types lo |Users enters first name and password|User logins successfully if name and password are correct|
|User types ex  |No input required        |User exits|
## Technologies Used
* Python 3.8.2
## Support and contact details
You are free to suggest and improve the code. To make your changes:
* Fork the repo
* Create a new branch
* Test, add, commit, and push your changes to the branch
* Create a pull request
* You can also contact the creator via this email address: njihiamary11@gmail.com
### License
MIT MIT License Copyright (c) 2020 Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions: The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software. THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE Copyright (c) 2020 Waithera-m