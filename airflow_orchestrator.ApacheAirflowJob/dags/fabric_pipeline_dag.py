from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.bash import BashOperator

default_args = {
    'owner': 'data_engineering',
    'depends_on_past': False,
    'start_date': datetime(2026, 1, 1),
    'email_on_failure': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

with DAG(
    'dp700_fabric_orchestration',
    default_args=default_args,
    description='Orchestrate Fabric Pipelines via Airflow',
    schedule_interval='@daily',
    catchup=False,
) as dag:

    start_task = BashOperator(
        task_id='start_job',
        bash_command='echo "Starting Fabric Orchestration Job..."',
    )

    end_task = BashOperator(
        task_id='end_job',
        bash_command='echo "Fabric Orchestration Completed Successfully."',
    )

    start_task >> end_task