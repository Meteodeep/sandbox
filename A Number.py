import random

number=random.randint(0,50)
number= (int(number))

count = 0

while(count < 5):
    
    
    mynumber=(int(input("Guess the Number?")))

    if mynumber < numberone:
        print("HIGHER")
        count = count + 1

    elif mynumber > numberone:
        print("LOWER")
        count = count + 1

    elif mynumber == numberone:
        print("WELL DONE!")






