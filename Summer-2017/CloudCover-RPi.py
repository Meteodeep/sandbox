from sense_hat import SenseHat

sense = SenseHat()
sense.clear()

temp = sense.get_temperature()

humidity = sense.get_humidity()

humidity = round(humidity, 1)

calc = 100-humidity

calc2 = calc/5

dewpoint = temp - calc2

depression = temp - dewpoint

cloudcover = depression * 400

cloudcover = cloudcover * 0.3048

cloudcover = (str(cloudcover))

print(cloudcover + "m")
