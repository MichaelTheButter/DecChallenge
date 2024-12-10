from extractor import Coordinates, MeteoClient, ForecastConverter
from file_loader import S3_Controller
from datetime import datetime


def main():
    AWS_S3_BUCKET_NAME = 'pkm-bucket'

    coordinates = Coordinates()
    meteo_client = MeteoClient()

    meteo_client.set_request_param(coordinates)
    forecast = meteo_client.get_forecast()

    forecast_df = ForecastConverter.hourly_as_pandas(forecast)
    file_name = datetime.now().strftime("%m-%d-%Y_%H:%M:%S")

    S3_Controller.save_df_as_csv(forecast_df, AWS_S3_BUCKET_NAME, file_name)


if __name__ == '__main__':
    main()