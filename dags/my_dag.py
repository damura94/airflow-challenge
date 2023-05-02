from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime, timedelta
import pandas as pd

# Definir argumentos por defecto
default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2023, 5, 1),
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

# Definir la función para extraer los datos
def extract_data():
    df = pd.read_csv('../data/Traffic_Flow_Map_Volumes.csv')
    return df

# Definir la función para limpiar y transformar los datos
def clean_and_transform_data(df):
    # Eliminar filas con valores faltantes
    df.dropna(inplace=True)

    # Calcular el número total de accidentes por tipo de clima
    accidents_by_weather = df.groupby('WEATHER')['OBJECTID'].count().reset_index()
    accidents_by_weather.rename(columns={'OBJECTID': 'TOTAL_ACCIDENTS'}, inplace=True)

    return accidents_by_weather

# Definir la función para exportar los datos transformados
def export_data(df):
    df.to_csv('../data/data_transformed.csv', index=False)

# Crear el DAG
dag = DAG(
    'my_dag',
    default_args=default_args,
    description='Pipeline de datos que extrae, transforma y exporta datos',
    schedule_interval=timedelta(days=1),
)

# Definir las tareas
t1 = PythonOperator(
    task_id='extract_data',
    python_callable=extract_data,
    dag=dag,
)

t2 = PythonOperator(
    task_id='clean_and_transform_data',
    python_callable=clean_and_transform_data,
    dag=dag,
)

t3 = PythonOperator(
    task_id='export_data',
    python_callable=export_data,
    dag=dag,
)

# Definir las dependencias entre las tareas
t1 >> t2 >> t3

