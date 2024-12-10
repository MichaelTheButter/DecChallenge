import openmeteo_requests

import requests_cache
import pandas as pd
from pandas.core.interchange.dataframe_protocol import DataFrame
from retry_requests import retry


class Coordinates:
	LATITUDE = "latitude"
	LONGITUDE = "longitude"

	def __init__(self):
		self.latitude: float = Coordinates.take_input(Coordinates.LATITUDE)
		self.longitude: float = Coordinates.take_input(Coordinates.LONGITUDE)

	@staticmethod
	def take_input(parameter: str) -> float:
		return float(input(f"Enter {parameter}: "))

	def as_dict(self):
		return {Coordinates.LATITUDE: self.latitude,
				Coordinates.LONGITUDE: self.longitude}


class MeteoClient:
	URL = "https://api.open-meteo.com/v1/forecast"

	def __init__(self, cache_name: str = '.cache', expire_after: int = 3600, retries: int = 5):
		# Setup the Open-Meteo API client with cache and retry on error

		self.cache_session = requests_cache.CachedSession(cache_name, expire_after=expire_after)
		self.retry_session = retry(self.cache_session, retries=retries, backoff_factor=0.2)
		self.openmeteo = openmeteo_requests.Client(session=self.retry_session)

	def set_request_param(self, coordinates: Coordinates, additional_parameters: dict = {"hourly": "temperature_2m", "timezone": "auto"}):
		self.coordinates = coordinates
		self.parameters = self.coordinates.as_dict() | additional_parameters

	def get_forecast(self):
		responses = self.openmeteo.weather_api(MeteoClient.URL, params=self.parameters)
		return responses[0]


class ForecastConverter:

	@staticmethod
	def hourly_as_pandas(response) -> DataFrame:

		hourly = response.Hourly()
		hourly_temperature_2m = hourly.Variables(0).ValuesAsNumpy()

		hourly_data = {"date": pd.date_range(
			start=pd.to_datetime(hourly.Time(), unit="s", utc=True),
			end=pd.to_datetime(hourly.TimeEnd(), unit="s", utc=True),
			freq=pd.Timedelta(seconds=hourly.Interval()),
			inclusive="left"
		)}
		hourly_data["temperature_2m"] = hourly_temperature_2m

		return pd.DataFrame(data=hourly_data)

	@staticmethod
	def print_param(response):

		print(f"Coordinates {response.Latitude()}°N {response.Longitude()}°E")
		print(f"Elevation {response.Elevation()} m asl")
		print(f"Timezone {response.Timezone()} {response.TimezoneAbbreviation()}")
		print(f"Timezone difference to GMT+0 {response.UtcOffsetSeconds()} s")