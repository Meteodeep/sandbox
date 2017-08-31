import webbrowser
from time import sleep

print(" V = I x R")
sleep(2)
webbrowser.open_new_tab("http://www.electronics-tutorials.ws/dccircuits/dcp3.gif")
sleep(4)

menu=input("What would you like to find: Voltage, Current or Resitance??")

menu = menu.lower()

if menu == "Volatage" or menu == "voltage":
    current=(float(input("Please enter your Current.. (in Amperes)")))
    resist=(float(input("Please enter your Resitance... (in Ohms)")))
    answer1 = current*resist
    answer1 = (str(answer1))
    print(answer1)

elif menu == "Current" or menu == "current":
    resist2=(float(input("Please enter your Resitance... (in Ohms)")))
    voltage=(float(input("Please enter your Voltage... (in Volts)")))
    answer2 = voltage/resist2
    answer2 = (str(answer2))
    print(answer2)

elif menu == "Resistance" or menu == "resistance":
    voltage2=(float(input("Please enter your Voltage.. (In Volts) ")))
    current2=(float(input("Please enter your given Current... (In Amperes)")))
    answer3 = voltage2/current2
    answer3 = (str(answer3))
    print(answer3)



