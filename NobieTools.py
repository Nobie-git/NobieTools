import os
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
    "\n[3] Placeholder",
    "\n[99] Exit program",
    "\n[0] Go back to title screen")
    inputVal = int(input())
    return inputVal
mainScreen()
def chatCounter():
    CharCInput = str(input("Please enter a string you'd like to get the character count of : "))
    print("Character count: ", len(CharCInput))
    input()
    mainScreen()
while "asd":
    if mainScreen() == 1:
        chatCounter()
    elif mainScreen() == 99:
        os.system("exit")
    elif mainScreen() == 0:
        mainScreen()
