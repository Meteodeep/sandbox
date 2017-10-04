import random

number=random.random()
numberone=10*number
numberone= (int(numberone))

count = 0

while(count < 4):
    
    
    mynumber=(int(input("Guess the Number?")))

    if mynumber < numberone:
        print("HIGHER")
        count = count + 1

    elif mynumber > numberone:
        print("LOWER")
        count = count + 1

    elif mynumber == numberone:
        print("WELL DONE!")






