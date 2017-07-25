class TropicalStorm(object):
    """A class that makes various tasty fruits."""
    def __init__(storm, name, pressure, windgust, hurricane):
        storm.name = name
        storm.pressure = pressure
        storm.windgust = windgust
        storm.hurricane = hurricane

    def description(storm):
        print("A %s %s with Wind Gusts of %s."  % (storm.pressure, storm.name, storm.windgust))

    def is_hurricane(storm):
        if storm.hurricane:
            print("Yes! Current Hurricane.")
        else:
            print("Currently not a Hurricane.")

sandy = TropicalStorm("Storm", "976hPa", "198km/h", False)

sandy.description()
sandy.is_hurricane()
