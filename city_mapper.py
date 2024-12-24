from extractor import Coordinates

class CityMapper:
    CITY_COORDINATES = {
        "Warsaw": (52.2297, 21.0122),
        "Krakow": (50.0647, 19.9450),
        "Lodz": (51.7592, 19.4560),
        "Wroclaw": (51.1079, 17.0385),
        "Poznan": (52.4064, 16.9252),
        "Gdansk": (54.3520, 18.6466),
        "Szczecin": (53.4285, 14.5528),
        "Bydgoszcz": (53.1235, 18.0084),
        "Lublin": (51.2465, 22.5684),
        "Katowice": (50.2649, 19.0238)
    }

    @staticmethod
    def get_city_name(latitude: float, longitude: float) -> str:
        for city, coords in CityMapper.CITY_COORDINATES.items():
            if coords == (latitude, longitude):
                return city
        return "Unknown"

    @staticmethod
    def get_coordinates(city: str) -> Coordinates:
        for city_name, coords in CityMapper.CITY_COORDINATES.items():
            if city_name == city:
                return Coordinates(latitude=coords[0], longitude=coords[1])
        return Coordinates(latitude=0, longitude=0)

    @staticmethod
    def get_cities() -> list:
        return list(CityMapper.CITY_COORDINATES.keys())

class CityInput:

    @staticmethod
    def take_input() -> str:
        print(f"Available cities: {CityMapper.get_cities()}")
        city = input("Enter city: ")
        return city

