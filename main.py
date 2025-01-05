from extractor import Coordinates, MeteoClient, ForecastConverter
from file_loader import S3Controller
from city_mapper import CityMapper, CityInput


def main():

    city = CityInput.take_input()
    coordinates = CityMapper.get_coordinates(city)
    meteo_client = MeteoClient()

    meteo_client.set_request_param(coordinates)
    forecast = meteo_client.get_forecast()

    forecast_df = ForecastConverter.hourly_as_pandas(forecast)
    forecast_df['city'] = city

    file_name = S3Controller.get_file_name(city)
    S3Controller.save_df_as_json(forecast_df, file_name)

if __name__ == '__main__':
    main()