from pandas import DataFrame
from datetime import datetime
from config import AwsCredentials

AWS_S3_BUCKET_NAME = 'pkm-bucket'
AWS_REGION = 'eu-west-3'

class S3Controller:

    @staticmethod
    def get_file_name(city: str) -> str:
        timestamp_str = datetime.now().strftime("%m%d%Y_%H%M%S")
        return f'{city}_{timestamp_str}'

    @staticmethod
    def save_df_as_csv(df: DataFrame, bucket_name: str, file_name: str):
        df.to_csv(
            f"s3://{bucket_name}/{file_name}",
            index=False,
            storage_options={
                "key": AwsCredentials.ACCESS_KEY,
                "secret": AwsCredentials.SECRET_KEY
            }
        )

    @staticmethod
    def save_df_as_json(df: DataFrame, file_name: str, to_s3: bool = False):
        if to_s3:
            df.to_json(
                f"s3://{AWS_S3_BUCKET_NAME}/{file_name}.json",
                orient='records',
                storage_options={
                    "key": AwsCredentials.ACCESS_KEY,
                    "secret": AwsCredentials.SECRET_KEY,
                    "region": AWS_REGION
                }
            )
        else:
            df.to_json(f"raw_json/{file_name}.json", orient='records')


