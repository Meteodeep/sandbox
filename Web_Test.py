#WebAI
#WebAI can also be used to edit 'index.html' firmware so users can interact with live, Real-Time Updates from the homepage, but as the sysytem is still a beta we are testing it in a more controlled enviroment


from time import sleep
import webbrowser
from sense_hat import SenseHat

f = open('weatheralerts.html','w')

message = """<html>
<head></head>
<body><h1 style="color:red; font-size:300%;">Weather</h1><br><iframe src="https://giphy.com/embed/UmPl68cxazEgo" width="480" height="120" frameBorder="0" class="giphy-embed" allowFullScreen></iframe><p><a href="https://giphy.com/gifs$
</html>"""

f.write(message)
f.close()


while True:

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

        if pressure <= "990" or temp <= "0" or temp >= "30" or humidity <= "20" or humidity >= "97":
            webbrowser.open_new_tab("weatheralerts.hml")
            


