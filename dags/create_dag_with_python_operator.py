from datetime import datetime, timedelta

from airflow import DAG
from airflow.operators.python import PythonOperator

default_args={
    'owner':'shreyas',
    'retries': 5,
    'retry_delay': timedelta(minutes=5)
}

def greet(name,age):
    print(f"Hello World! My name is {name} and I am {age} years old.")

with DAG(
    default_args= default_args,
    dag_id= 'our_first_dag_with_python_operator_v2',
    description= 'Our first dag using python operator',
    start_date= datetime(2024,8,25, 4),
    schedule_interval='@daily'

) as dag:
    
    task_1= PythonOperator(
        task_id='greet',
        python_callable= greet,
        op_kwargs={'name':'Steven Strange', 'age':50}
    )

    task_1