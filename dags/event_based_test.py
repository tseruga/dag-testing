from datetime import timedelta
from datetime import date
from airflow.utils.dates import days_ago

from airflow import DAG
from airflow.providers.amazon.aws.sensors.s3_prefix import S3PrefixSensor

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

dag = DAG(
    'event_based',
    default_args=default_args,
    description='Example cron DAG',
    start_date=days_ago(1),
    schedule_interval=None,
    max_active_runs=1
)

watch_drop_prefix = S3PrefixSensor(
    bucket_name='file-drops',
    prefix='raw/',
    aws_conn_id='minio-conn',
    dag=dag
)

watch_drop_prefix
