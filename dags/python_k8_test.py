from datetime import timedelta

from airflow import DAG
from airflow.providers.cncf.kubernetes.operators.kubernetes_pod import KubernetesPodOperator

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

dag = DAG(
    'python_k8_pod_testing',
    default_args=default_args,
    description='Example cron DAG',
    schedule_interval=timedelta(days=1),
)

t1 = KubernetesPodOperator(
    namespace='default',
    image='python:3-buster',
    cmds=['python', '-c', "print('Hello world!')"],
    is_delete_operator_pod=True,
    in_cluster=True,
    task_id="hello-world",
    get_logs=True,
    name="python-task-pod",
    dag=dag
)
