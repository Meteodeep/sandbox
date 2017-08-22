from sense_hat import SenseHat

sense = SenseHat()
sense.clear()

temp = sense.get_temperature()

humidity = sense.get_humidity()

humidity = round(humidity, 1)

calc = 100-humidity

calc2 = calc/5

dewpoint = temp - calc2

dewpoint = (str(dewpoint)

print(dewpoint + " degrees C")
