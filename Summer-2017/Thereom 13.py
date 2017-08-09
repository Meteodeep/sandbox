import math

while True:

    print("Co-Ordinate Geometry")

    y1=(int(input("Please enter Y1")))
    y2=(int(input("Please enter Y2")))
    x1=(int(input("Please enter X1")))
    x2=(int(input("Please enter X2")))


    menu=input("Find the Slope OR Length OR Midpoint")

    if menu == "Length":
        one = x2-x1**2
        two = y2-y1**2
        length = math.sqrt(one+two)
        print(length)

    elif menu == "Slope":
        three = y2-y1
        four = x2-x1
        slope = three/four
        print(slope)

    elif menu == "Midpoint":
        five = x1+x2
        six = y1+y2
        x = five/2
        y = six/2
        print(x + y)
        
        
        
        



