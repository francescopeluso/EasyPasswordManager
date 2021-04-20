"""
Password Generator v1.2
by Francesco Peluso - 20/04/2021
"""

import random
import json

filename = 'local_archive.json'

# define a function to write data on JSON file
def write_json(data, filename):
    with open(filename,'w') as f:
        json.dump(data, f, indent=4)

# create strings with characters that we want to be used
chars       = "abcdefghijklmnopqrstuvwxyz"
charsCaps   = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers     = "0123456789"
punctuation = "!$%&/()=@#*[]\{\}"

# little header on script start
print("\n+----------------------------------------------+")
print("|         Easy Password Generator v1.2         |")
print("|     by Francesco Peluso - @thatsfrankie      |")
print("+----------------------------------------------+")

# ask user how much the password has to be long
passLength = input("\nHow much long the password has to be? >> ")

# generate password by picking randomly the characters
password = random.choices(chars+charsCaps+numbers+punctuation, k = int(passLength))
password = "".join(password)

print("\nYour password is: " + password)

# adding password to "a local database"
print("\n\nWould you like to associate this password with one of you accounts?")
answer = input("[Insert the name of the platform, or leave blank] >> ")

if answer != "":
    with open(filename) as json_file:
        data = json.load(json_file)
        
        temp = data['passwords_list']
    
        # python object to be appended
        x = {"platform": answer,
             "password": password,
            }

        # appending data to passwords_list
        temp.append(x)

    write_json(data, filename)
    print ("\nYour password has been associated!")
else:
    with open(filename) as json_file:
        data = json.load(json_file)
        
        temp = data['unassociated_passwords']

        # appending data to unassociated_passwords
        temp.append(password)

    write_json(data, filename)
    print ("\nOK. Remember that you can still find this password in the 'unassociated' section")
