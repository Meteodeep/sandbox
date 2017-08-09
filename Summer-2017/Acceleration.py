velocitystart=(int(input("Please enter the Velocity at the Start (in m/s^2)")))
velocityfinish=(int(input("Please enter the Velocity at the Finish (in m/s^2)")))
time=(int(input("Please enter the Time (in Seconds)")))

velocitychange = velocityfinish-velocitystart
acceleration = velocitychange/time

acceleration = (str(acceleration))

print(acceleration + "m/s^2")
