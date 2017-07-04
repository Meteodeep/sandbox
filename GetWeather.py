
while True:
        from time import sleep

        from sense_hat import SenseHat

        sense = SenseHat()
        sense.clear()

        pressure = sense.get_pressure()
        pressure = round(pressure, 1)
        pressure = str(pressure)

        temp = sense.get_temperature()
        temp = round(temp,1)
        temp = str(temp)

        humidity = sense.get_humidity()
        humidity = round(humidity, 1)
        humidity = str(humidity)
