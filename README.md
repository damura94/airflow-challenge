#Proyecto de Airflow Challenge
Este es un proyecto de ejemplo para utilizar Apache Airflow en un flujo de trabajo simple de extracción, transformación y carga de datos.

#Dependencias
Este proyecto tiene las siguientes dependencias:

Docker (versión 20.10 o superior)
Docker Compose (versión 1.29 o superior)
Acceso a internet para descargar paquetes y dependencias de Python


#Estructura del proyecto
La estructura del proyecto es la siguiente:


airflow-challenge/
├── dags/
│   ├── my_dag.py
├── data/
│   ├── input.csv
├── scripts/
│   ├── extract_data.py
│   ├── transform_data.py
│   ├── export_data.py
├── docker-compose.yml
├── Dockerfile
└── entrypoint.sh
└── README.md

*La carpeta dags contiene el archivo my_dag.py, que define el flujo de trabajo de Apache Airflow.
*La carpeta data contiene el archivo input.csv, que es el archivo de entrada para el flujo de trabajo.
*La carpeta scripts contiene los scripts Python utilizados para la extracción, transformación y carga de datos.
*El archivo docker-compose.yml define los servicios de Docker necesarios para ejecutar el flujo de trabajo.
*El archivo Dockerfile define la imagen Docker para el contenedor de Apache Airflow.
*El archivo entrypoint.sh es el punto de entrada del contenedor de Apache Airflow.
*README.md: este archivo.


#Instrucciones de uso
Para ejecutar el flujo de trabajo, siga los siguientes pasos:

*Clone este repositorio en su máquina local.
*Asegúrese de tener Docker y docker-compose instalados en su máquina.

*Clona este repositorio en tu máquina local con el siguiente comando.
	git clone https://github.com/damura94/airflow-challenge.git
*Desde la carpeta raíz del proyecto, ejecute el comando para crear los contenedores de Docker.
	 docker-compose build
*Desde la carpeta raíz del proyecto, ejecute el comando para iniciar los contenedores de Docker.
	docker-compose up -d
*Abra su navegador y vaya a http://localhost:8080 para acceder a la interfaz de usuario de Apache Airflow.
*En la pestaña "DAGs" en la interfaz de usuario, habilite el flujo de trabajo haciendo clic en el botón de encendido en la fila de "my_dag".
*Haga clic en el nombre del flujo de trabajo para ver más detalles y ejecutarlo haciendo clic en el botón de "Trigger DAG".


¡Y eso es todo! El flujo de trabajo se ejecutará automáticamente y los resultados se guardarán en la carpeta data.

Notas
El DAG my_dag está programado para ejecutarse una vez al día a medianoche. Puedes ajustar la programación cambiando los valores de las variables en el código de my_dag.py.
Este proyecto de ejemplo solo realiza una transformación de datos simple. Si tu pipeline de datos es más complejo, puedes agregar más tareas y operadores a tu DAG en my_dag.py.
Asegúrate de tener suficiente espacio en disco disponible en tu máquina local para los archivos de datos que se generan como resultado del pipeline.