
temp=(int(input("Please enter the Current Air Temperature (in Degrees C)")))
humidity=(int(input("Please enter the current Humidity (from %)")))

calc = 100-humidity

calc2 = calc/5

dewpoint = temp - calc2

depression = temp - dewpoint

cloudcover = depression * 400

cloudcover = cloudcover * 0.3048

cloudcover = (str(cloudcover))

print(cloudcover + "m")
