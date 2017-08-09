radius=(int(input("Please enter the Radius (in cm)")))

menu=input("Area or Volume???")

if menu == "Area":
    
    area = 4*3.141*radius**2
    area = (str(area))

    print(area + "cm^2")

elif menu == "Surface":

    math = 4/3
    volume = math*3.141*radius**3
    volume = (str(volume))

    print(volume + "cm^3")
