from tkinter import *
from tkinter import filedialog

import json

from Crypto import PublicKey

from classes.User import User
from classes.Signature import *


CreateNewAccount = str(input("Do you want to CreateNew Account or not [Y/N] ")).upper()

if CreateNewAccount == 'Y':
    u = User()
    Username = str(input("Please Input Your Username : "))
    while u.AccountExisted(Username):
        print("Account Existed Please Tryagain")
        Username = str(input("Please Input Your Username : "))
    
    print("Account Created Please Select location to stored your Private Key")
    PrivateKeyFilePath = filedialog.asksaveasfilename(filetypes=[("Json", '*.json'), ("All files", "*.*")]) + ".JSON"
    u.CreateNewUser(Username, PrivateKeySavedLocation=PrivateKeyFilePath)

if CreateNewAccount == 'N':
    SOV = str(input("Do you want to Sign or Verify [S/V] ")).upper()
    
    if SOV == 'S':
        print("Please Select your PrivateKey file destination")
        PrivateKeyFilePath = filedialog.askopenfile()
        with open(PrivateKeyFilePath.name) as jsonfile:
            PrivateKey = json.load(jsonfile)
            
        print("Please Select File to sign")
        FilePath = filedialog.askopenfile()
        message_hash = CreateMessage(FilePath=FilePath.name)
        
        signature = Sign(message_hash, PrivateKey)
        print("Your Signature is")
        print(signature)

    if SOV == 'V':
        print("Please Select Signed File")
        FilePath = filedialog.askopenfile()
        message_hash = CreateMessage(FilePath=FilePath.name)

        u = User()
        Username = str(input("Please input signature Owner Account : "))
        while not u.AccountExisted(Username):
            print("Account Not Found Tryagain")
            Username = str(input("Please Input Your Username : "))
        
        PublicKey = u.GetPublicKey(Username)
        
        print("Please Input signed Signature")
        signature = int(input())

        if Verify(message_hash, signature, PublicKey):
            print("Verification Passed")
        else:
            print("Verification Failed")
