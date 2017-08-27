velocitystart=(float(input("Please enter the Velocity at the Start (in m/s^2)")))
velocityfinish=(float(input("Please enter the Velocity at the Finish (in m/s^2)")))
time=(float(input("Please enter the Time (in Seconds)")))

velocitychange = velocityfinish-velocitystart
acceleration = velocitychange/time

acceleration = (str(acceleration))

print(acceleration + "m/s^2")
