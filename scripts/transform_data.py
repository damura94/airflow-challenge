import pandas as pd

def clean_and_transform(df):
    # Eliminar filas con valores faltantes
    df.dropna(inplace=True)

    # Calcular el número total de accidentes por tipo de clima
    accidents_by_weather = df.groupby('WEATHER')['OBJECTID'].count().reset_index()
    accidents_by_weather.rename(columns={'OBJECTID': 'TOTAL_ACCIDENTS'}, inplace=True)

    return accidents_by_weather
