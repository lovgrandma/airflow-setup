from airflow import DAG
from airflow.operators.dummy_operator import DummyOperator
from airflow.operators.bash_operator import BashOperator
from airflow.operators.python_operator import PythonOperator  # Import PythonOperator
from datetime import datetime

# Define the function to be executed at DAG startup
def run_on_startup():
    print("Running redis instances")

def step2():
    print("Ran redis instance complete")

default_args = {
    'owner': 'airflow',
    'retries': 1,
    'start_date': datetime(2024, 1, 1),
}

dag = DAG(
    'redis_startup',
    default_args=default_args,
    description='Run redis instances on machine start',
    schedule_interval='@once',  # Only run once on startup
    catchup=False,
)

# PythonOperator for the function that runs on startup
run_python_task = PythonOperator(
    task_id='run_python_on_startup',
    python_callable=run_on_startup,  # Call the function here
    dag=dag,
)

# BashOperator to run the bash command (ensure correct path and quotes)
run_bash_command = BashOperator(
    task_id='run_script_on_startup',
    bash_command='cd /Users/jessethompson/Projects/redis && ./runredis &',
    dag=dag,
)

run_step2 = PythonOperator(
    task_id='step2_task',
    python_callable=step2,  # Call the step2 function
    dag=dag,
)

# Define the start task (optional)
start = DummyOperator(task_id='start', dag=dag)

# Set task dependencies (ensure the order of task execution)
start >> run_python_task >> run_bash_command >> run_step2 # Python first, then Bash
