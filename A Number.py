import random

number=random.randint(0,50)
number= (int(number))

count = 0

while(count < 6):
    
    
    mynumber=(int(input("Guess the Number?")))

    if mynumber < number:
        print("HIGHER")
        count = count + 1

    elif mynumber > number:
        print("LOWER")
        count = count + 1

    elif mynumber == number:
        print("WELL DONE!")
        
print(random)






