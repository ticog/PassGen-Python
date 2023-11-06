import random
import string
import socket
import os
import hashlib

## Quick explanation of the app

print('\n---- Welcome to my Password Generator. ---- \n\nIf you need to reset your Password please delete your password.key file. \nShould be located in the same directory you run this app.')
password = input("\n[!] Please enter your Password! If this is your First time using this app you can set a password now!: ")

## Checks if a password file exists if not it creates one
## It also hashes it with the md5 algorithm for a better security :)
if "password.key" in os.listdir():
    pass
else:
    with open("password.key", "wb")as f:
        f.write(hashlib.md5(password.encode()).hexdigest().encode())

## Reads the hashed password in the file so it can validate it at the login
with open("password.key", "r")as f:
    passFileContent = f.readline().strip()

## Gets the local hostname
username = socket.gethostname()

## Login process
print(f"Hello {username}!")
if hashlib.md5(password.encode()).hexdigest() == passFileContent:
    pass
else:
    print("Wrong!")
    exit()

## Defining the password length
length = int(input("[!] HOW LONG SHOULD THE PWD BE?: "))

## Defining the allowed charactes and digits & grouping them all together
allowed_chars_Lower = (string.ascii_lowercase)
allowed_chars_Upper = (string.ascii_uppercase)
numbers = string.digits
allowed_Chars = allowed_chars_Lower + allowed_chars_Upper + numbers

passwd = []

## Randomizing each allowed character and digit.
for i in range(length):
    passwd.append(random.choice(allowed_Chars))

## Printing it to the console for the user.
print("".join(passwd))
print("\nThank you for using this app")