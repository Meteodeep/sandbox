while True:
	from time import sleep
	
	from sense_hat import SenseHat
	
	# Weather Reports

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

	# File Writing
	
	target1 = open('/var/www/pressure.txt', 'w')
	target1.write(pressure)
	target1.close()

	target2 = open('/var/www/temp.txt', 'w')
	target2.write(temp)
	target2.close()

	target3 = open('/var/www/humidity.txt', 'w')
	target3.write(humidity)
	target3.close()

	sleep(300) # 5 Minutes

	target1.truncate()
	target1.close()

	target2.truncate()
	target2.close()

	target3.truncate()
	target3.close()
