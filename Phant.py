########################################################################
# phant-raspi.py
# Raspberry Pi Phant Example
# Jim Lindblom @ SparkFun Electronics
# July 7, 2014
#
# This example demonstrates how to post data to a phant server (e.g.
#   data.sparkfun.com) using python on a Raspberry Pi.
#   The RPi.GPIO module is used to enable I/O reading and writing.
#   Before running this script, make sure to update your public and
#   private keys (publicKey and privateKey vars).
#
# Development environment specifics:
#   Raspberry Pi rev 2
#
# This code is beerware; if you see me (or any other SparkFun employee)
# at the local, and you've found our code helpful, please buy us a round!
# Distributed as-is; no warranty is given.
########################################################################

import RPi.GPIO as GPIO  # RPi.GPIO used for GPIO reading/writing
import time              # time used for delays
import httplib, urllib   # http and url libs used for HTTP POSTs
import socket            # socket used to get host name/IP

#################
## Phant Stuff ##
#################
server = "data.sparkfun.com" # base URL of your feed
publicKey = "6JZbNolApzF4om2l9yYK" # public key, everyone can see this
privateKey = "Ww0vPW1yrkUNDqWPV9jE"  # private key, only you should know
fields = ["light", "switch", "name"] # Your feed's data fields

######################
## I/O Stuff & Misc ##
######################
buttonPin = 22 # Active-low button connected to Broadcom pin 22
switchPin = 23 # SPST switch connected to Broadcom pin 23
myname = socket.gethostname() # Send local host name as one data field

##############
## I/O Setup #
##############
GPIO.setmode(GPIO.BCM) # Broadcom pin-numbering scheme
GPIO.setup(buttonPin, GPIO.IN, pull_up_down=GPIO.PUD_UP) # Button pin set as input w/ pull-up
GPIO.setup(switchPin, GPIO.IN, pull_up_down=GPIO.PUD_UP) # Switch set as input w/ pull-up

##########
## Loop ##
##########
print("Here we go! Press CTRL+C to exit")
try:
    # Loop until CTRL+C is pressed
    while 1:
        # If the button is pressed, we'll send our data. It's active-low
        # so we need to check if it's 0.
        if not (GPIO.input(buttonPin)):
            print("Sending an update!")
            # Our first job is to create the data set. Should turn into
            # something like "light=1234&switch=0&name=raspberrypi"
            data = {} # Create empty set, then fill in with our three fields:
            # Field 0, light, gets the local time:
            data[fields[0]] = time.strftime("%A %B %d, %Y %H:%M:%S %Z")
            # Field 1, switch, gets the switch status:
            data[fields[1]] = GPIO.input(switchPin)
            # Field 2, name, gets the pi's local name:
            data[fields[2]] = myname
            # Next, we need to encode that data into a url format:
            params = urllib.urlencode(data)

            # Now we need to set up our headers:
            headers = {} # start with an empty set
            # These are static, should be there every time:
            headers["Content-Type"] = "application/x-www-form-urlencoded"
            headers["Connection"] = "close"
            headers["Content-Length"] = len(params) # length of data
            headers["Phant-Private-Key"] = privateKey # private key header

            # Now we initiate a connection, and post the data
            c = httplib.HTTPConnection(server)
            # Here's the magic, our reqeust format is POST, we want
            # to send the data to data.sparkfun.com/input/PUBLIC_KEY.txt
            # and include both our data (params) and headers
            c.request("POST", "/input/" + publicKey + ".txt", params, headers)
            r = c.getresponse() # Get the server's response and print it
            print r.status, r.reason

            time.sleep(1) # delay for a second

except KeyboardInterrupt: # If CTRL+C is pressed, exit cleanly:
    GPIO.cleanup() # cleanup all GPIO
