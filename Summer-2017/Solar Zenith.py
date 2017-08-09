import math
n=(int(input("One Day out of the Whole Year")))

solar = 23.45*math.sin(360*284+n/365)

solar = (str(solar))

print(solar)
