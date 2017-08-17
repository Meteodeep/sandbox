from time import sleep
temp=(int(input("Please enter the Current Air Temperature (in Degrees C)")))
humidity=(int(input("Please enter the current Humidity (from %)")))

calc = 100-humidity

calc2 = calc/5

dewpoint = temp - calc2

print(dewpoint)

sleep(25)
