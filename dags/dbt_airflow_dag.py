from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime, timedelta

default_args = {
    'owner': 'mahima0099',
    'retries': 1,
    'retry_delay': timedelta(minutes=5)
}

with DAG(
    dag_id='dbt_transformation_dag',
    default_args=default_args,
    description='Run DBT project using Airflow',
    start_date=datetime(2023, 1, 1),
    schedule_interval=None,
    catchup=False
) as dag:

    run_dbt = BashOperator(
        task_id='run_dbt_project',
        bash_command='cd /home/mahima0099/repos/demo/dbt/project_ms_airflow && dbt run'
    )
