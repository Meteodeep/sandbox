s = "Atmosphere"
if s.find("sphere") == -1:
    print("No 'sphere' here!")
else:
    print("Found 'sphere' in the string.")


s2 = "Convection causes Thunderstorms"
for word in s2.split():
        print(word)

pressure = '987hPa'
windgust = '124km/h'


print("Lowest Pressure for storm is %s and highest wind gust: %s  " % (pressure, windgust))


