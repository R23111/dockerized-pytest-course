

class Point():
    def __init__(self, name, latitude, longitude):

        if not type(name) is str:
            raise TypeError("Name should be a str")

        self.name = name

        if not (-90 <= latitude <= 90) or not (-180 <= longitude <= 180):
            raise ValueError("Invalid latitude, longitude combination.")
        self.latitude = latitude
        self.longitude = longitude


    def get_lat_long(self):
        return (self.latitude, self.longitude)
