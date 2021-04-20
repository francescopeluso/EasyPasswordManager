"""
Easy Password Generator v1.5
by Francesco Peluso - 20/04/2021
"""

import random
import json
import os
import time

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

def screen_clear():
    if os.name == 'posix':
        # if script is running on mac or linux/unix
        _ = os.system('clear')
    else:
        # for windows platfrom
        _ = os.system('cls')

def generate_password():
    # ask user how much the password has to be long
    passlength = input("\nHow much long the password has to be? >> ")

    # generate password by picking randomly the characters
    password = random.choices(chars+charsCaps+numbers+punctuation, k = int(passlength))
    password = "".join(password)

    print("\nYour password is: " + password)

    # adding password to "a local database"
    print("\n\nWould you like to associate this password with one of you accounts?")
    answer = input("[Insert the name of the platform, or leave blank] >> ")
    register_password(answer, password)


def register_password(answer, password):
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
        time.sleep(3)
    else:
        with open(filename) as json_file:
            data = json.load(json_file)
            
            temp = data['unassociated_passwords']

            # appending data to unassociated_passwords
            temp.append(password)

        write_json(data, filename)
        print ("\nOK. Remember that you can still find this password in the 'unassociated' section")
        time.sleep(3)
    screen_clear()

def view_passwords():
    with open(filename) as json_file:
        data = json.load(json_file)

        print("\n\n Here's the password associated with each platform:")
        print(" (if output is blank, there are none of these passwords)")
        for _ in data['passwords_list']:
            print("     ", _)

        print("\n\n Here's the unassociated passwords, instead:")
        print(" (if output is blank, there are none of these passwords)")
        for _ in data['unassociated_passwords']:
            print("     ", _)

    _ = input("\n Press a key to go back to main screen...")
    screen_clear()


# little header on script start
while True:
    print("\n+----------------------------------------------+")
    print("|         Easy Password Generator v1.5         |")
    print("|     by Francesco Peluso - @thatsfrankie      |")
    print("+----------------------------------------------+")

    print("\nWhat would you like to do?")
    print("    1. Generate a new password.")
    print("    2. View all your password.")
    print("    0. Exit the program.")

    select = input("\n  Make a choice >> ")

    if select == "1":
        generate_password()
    elif select == "2":
        view_passwords()
    elif select == "0":
        exit()
    else:
        print(" \nThe choice made isn't valid.")
        time.sleep(3)
        screen_clear()