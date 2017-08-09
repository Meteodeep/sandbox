import math
t=(int(input("Please enter the Temperature (in Degrees C)")))
w=(int(input("Please enter the Wind Speed (in km/h)")))

windchill = 13.12+0.6215*t-11.37*w**0.16+0.3965*t**0.16

windchill = (str(windchill))

print(windchill + "C")
