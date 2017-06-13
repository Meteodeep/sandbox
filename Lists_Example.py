from time import sleep
import webbrowser
from datetime import datetime


def program():  
        
    maths=(int(input("Please enter a number.......")))

    while True:

        hence=input("Would you like to multiply (by 10) or continue")

        if hence == "multiply" or hence == "Multiply":
            print("Okay")
            ans = maths*10
            ans = (str(ans))
            print("Ans:" + ans)

        else:
            break



    print("pi=3.14")
    sleep(5)

    sci = ['Melt' , 'Evaporate' , 'Freeze']
    print(sci)
    len(sci)
    print("Spot the mistake........3 Seconds!")
    sleep(3)
    what=input("What is it!?!?!")
    sci.insert(2,what)
    print("The Answer........")
    print("CONDENSE")
    sci.append("CONDENSE")
    print(sci)
    for type in sci:
        if type == "condense" or type == "Condense":
            print("WELL DONE!!!")
        else:
            print("Hard Luck...")


def area(height,width):
    it = height*width
    print (it)

    now = datetime.now()
    print(now)


psswrd=input("Please enter password to continue......")

if psswrd == "QWERTY":
    program()
    area(3,2)

if psswrd != "QWERTY":
    print("locked!")
    sleep(999999)
