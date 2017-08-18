#Elastic Potential
force=(int(input("Please enter the Force Applied (in Newtons)")))
x=(int(input("Please enter the length of the Unstretched Rope (in Metres)")))
xl=(int(input("Please enter the length of Stretched Rope (in Metres)")))

stretch = x-xl
elastic = 0.5*force*stretch

elastic = (str(elastic))

print(elastic)



