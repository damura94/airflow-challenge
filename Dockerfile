FROM apache/airflow:2.1.2-python3.8

USER root

RUN apt-get update \
    && apt-get install -y --no-install-recommends \
    postgresql-client \
    && apt-get autoremove -yqq --purge \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

COPY ./entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

USER airflow

ENV AIRFLOW_USERNAME=daniel
ENV AIRFLOW_PASSWORD=admin123
ENV AIRFLOW__WEBSERVER__AUTHENTICATE=True
ENV AIRFLOW__CORE__EXECUTOR=LocalExecutor
ENV AIRFLOW__CORE__SQL_ALCHEMY_CONN=postgresql+psycopg2://airflow:airflow@postgres:5432/airflow
ENV AIRFLOW__CORE__LOAD_EXAMPLES=False
ENV POSTGRES_USER=airflow
ENV POSTGRES_PASSWORD=airflow
ENV POSTGRES_DB=airflow

ENTRYPOINT ["/entrypoint.sh"]
CMD ["webserver"]
