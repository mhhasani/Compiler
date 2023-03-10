# check if an email is valid or not
import re

def is_valid_email(addr):
    if re.match(r'^[a-zA-Z0-9 _]+@[a-zA-Z0-9 _]+(\.[a-zA-Z0-9 _]+)+$', addr):
        return True
    else:
        return False

email = input('Please input your email address: ')  
if is_valid_email(email):
    print('Your email address is valid.')
else:
    print('Your email address is invalid.')