import random
import string
import socket
import os
import time
from cryptography.fernet import Fernet


if 'key.key' in os.listdir():
    print("True")
    pass  
else:
    print("False")
    key = Fernet.generate_key()
    with open('key.key', "wb") as filekey:
        filekey.write(key)

## Quick explanation of the app

print('\n---- Welcome to my Password Generator. ----')
print("\n Its recommended to Save the 'key.key' file somewhere safe.")
time.sleep(2)
## Gets the local hostname
username = socket.gethostname()

## Defining the password length
websiteUser = str(input("[!] WHATS THE USERNAME?: "))
website = str(input("[!] WHAT WEBSITE IS THIS PASSWORD FOR?: "))
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
print(f"\n\n[+] {website} : " + "".join(passwd))
website = "http://" + website + ".com"

with open('key.key', "rb")as filekey:
    key = filekey.read()

fernet = Fernet(key)

with open("credentials.txt", "a") as credFile:
    credFile.write(website + ":" + websiteUser + ":" + "".join(passwd) + "\n")

with open("credentials.txt", "rb") as contentToEncrypt:
    original_Content = contentToEncrypt.read()

encrypted = fernet.encrypt(original_Content)

with open('credentials.txt','wb') as encrypted_File:
    encrypted_File.write(encrypted)
    
    

print("\nThank you for using this app")
