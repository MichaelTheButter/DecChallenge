from pandas import DataFrame

from config import AwsCredentials

AWS_S3_BUCKET_NAME = 'pkm-bucket'
AWS_REGION = 'eu-west-3'

class S3_Controller:

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


