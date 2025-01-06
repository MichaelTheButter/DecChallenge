from extractor import MeteoClient, ForecastConverter
from file_loader import S3Controller
from city_mapper import CityMapper, CityInput
from  pipeline_config import get_spark_session
from json_to_parquet import collect_to_parquet
from loader import run_db_loader
import orchestrator

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

    if orchestrator.ask_to_run_spark_jobs():
        spark = get_spark_session()
        collect_to_parquet(spark)
        run_db_loader(spark)

if __name__ == '__main__':
    main()