import os
import random
from datetime import datetime
import time
import winsound

def mainScreen():
    os.system("cls")
    print("""
              \  |        |     _)            __ __|               |       
               \ |  _ \   __ \   |   _ \         |    _ \    _ \   |   __| 
             |\  | (   |  |   |  |   __/         |   (   |  (   |  | \__ \ 
            _| \_|\___/  _.__/  _| \___|        _|  \___/  \___/  _| ____/ 
    """, "\n                        Made by nobie :D (duh... ._.)", "\n\n\n",
    "\n[1] Char counter",
    "\n[2] Account generator",
    "\n[3] Timer",
    "\n[4] Leak Zablinga",
    "\n[99] Exit program",
    "\n[0] Go back to title screen")
    inputVal = int(input())
    return inputVal
mainScreen()
def countChars():
    CharCInput = str(input("Please enter a string you'd like to get the character count of : "))
    print("Character count: ", len(CharCInput))
    input("\n Press [ENTER] to go back to main screen.")
    mainScreen()
def accGen():
    now = datetime.now()
    timeFormat = now.strftime("%Y/%B/%d | %H:%M:%S")

    RBXCharTable = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',
    '1','2','3','4','5','6','7','8','9','0','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R',
    'S','T','U','V','W','X','Y','Z']

    usernameInput = int(input("How long do you want the username to be? (3-20) "))
    passInput = int(input("How long do you want the password to be? "))
    ammountOfAccounts = int(input("How many more do you want to make? (0 to make one)"))

    for ammountOfAccounts in range(0, ammountOfAccounts):
        username = ""
        password = ""
        if usernameInput >= 20:
            for i in range(0, 20):
                username = username + RBXCharTable[random.randint(0, len(RBXCharTable) - 1)]
            for i in range(0, passInput):
                password = password + chr(random.randint(20, 127))
        if usernameInput <= 20:
            for i in range(0, usernameInput):
                username = username + RBXCharTable[random.randint(0, len(RBXCharTable) - 1)]
            for i in range(0, passInput):
                password = password + chr(random.randint(20, 127))
        print("Username: " + username, "\nPassword: " + password, "\n=-=--=- ["+ timeFormat +"] -=-=-=")
        with open("Accounts.txt", "a") as fileobj:
            fileobj.write("Username: " + username + "\nPassword: " + password + "\n=-=--=- ["+ timeFormat +"] -=-=-=\n")
    print("\n\nAccounts saved to Accounts.txt sucessfully!")
    input("\n Press [ENTER] to go back to main screen.")
def Timer():
    mins = int(input("How many minutes minutes : "))
    sec = int(input("How many seconds :"))
    minsec = mins * 60 + sec
    for i in range(1, minsec + 1):
        print(i)
        time.sleep(1)
        if i == minsec:
            winsound.Beep(1000, 1000)
            input("\n Press [ENTER] to go back to main screen.")
while "asd":
    if mainScreen() == 1:
        countChars()
    elif mainScreen() == 99:
        os.system("exit")
    elif mainScreen() == 0:
        mainScreen()
    elif mainScreen() == 2:
        accGen()
    elif mainScreen() == 3:
        Timer()
    elif mainScreen() == 4:
        print("Never.")
