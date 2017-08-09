import math
f=(int(input("Please enter the Frequency at Rest")))
vs=(int(input("Please enter the Velocity of the Source")))

velocity = 340-vs

math = 340/velocity

doppler = math*f

print(doppler)
