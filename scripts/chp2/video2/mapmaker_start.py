class Point():
    def __init__(self, city: str, lat: float, long: float) -> None:
        self._city = city
        self._lat = lat
        self._long = long

    def get_lat_long(self) -> tuple:
        return (self._lat, self._long)
