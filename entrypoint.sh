#!/bin/bash
airflow db init
#!/bin/bash

# Print the command that is being executed
echo "Executing: flask fab create-user -f /config/connections.yaml"

# Create the user
flask fab create-user -f /config/connections.yaml

# Start the webserver
airflow webserver

airflow users create \
    --username admin \
    --firstname admin \
    --lastname admin \
    --email admin@example.com \
    --password admin \
    --role Admin
airflow scheduler &
exec airflow webserver
