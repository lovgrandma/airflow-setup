# Create env
python -m venv airflow_env

# Activate env
source airflow_env/bin/activate

# Init db. Should create a simple sqlite db
airflow db init

# Start server
airflow webserver --port 8080

# Open another terminal and start scheduler
airflow scheduler

# Edit your system dags at ~/airflow/dags
touch ~/airflow/dags <dag>

# View interface
http://localhost:8080/

# Run a dag 
airflow dags trigger hello_world

# Create user
airflow users create \
    --username admin \
    --firstname Jesse \
    --lastname Thompson \
    --role Admin \
    --email jessethompson@tycoon.systems