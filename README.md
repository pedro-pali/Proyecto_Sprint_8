# Proyecto_Sprint_8
Simulación de estar trabajando para una empresa de análisis de taxis en la ciudad de Chicago, USA. Encontrando patrones en la información de la base de datos del mes de noviembre del 2017. Comparando datos de competidores y generar una hipótesis de cómo afecta el clima al resultado total de los servicios de taxis.

## Paso 1. Extracción de datos de la página web como un DataFrame
Escribimos el código para analizar los datos sobre el clima en Chicago en noviembre de 2017, desde el sitio web:
https://practicum-content.s3.us-west-1.amazonaws.com/data-analyst-eng/moved_chicago_weather_2017.html

## Paso 2. Análisis exploratorio 

## Paso 3.

## Paso 4. Análisis exploratorio (Python)
Tenemos dos archivos .csv recuperados en los pasos anteriores:
- El primero ..._resul_01.csv contiene dos columnas y lo llamaremos 'df_1':
-- company_name: nombre de la empresa de taxis 
-- trips_amount: el número de viajes de cada compañía de taxis el 15 y 16 de noviembre de 2017.
- El segundo ..._result.csv contiene dos columnas y lo llamaremos 'df_4':
-- dropoff_location_name: barrios de Chicago donde finalizaron los viajes
-- average_trips: el promedio de viajes que terminaron en cada barrio en noviembre de 2017.
Resumen de análisis hecho:
 - Importación de archivos,
 - convertir los datos necesarios, 
 - identificación de los 10 principales barrios en términos de finalización del recorrido,
 - gráficos de barra para vidualización y comparativa, y
 - conclusiones de los resultados.

 ## Paso 5. Prueba de hipótesis (Python)
 Hipotesis de duración promedio de viajes, los cuales vienen en el archivo ..._result_07 al cual llamamos 'df_07' y contiene:
 -- start_ts: fecha y hora de la recogida
 -- weather_conditions: condiciones climáticas en el momento en el que comenzó el viaje
 -- duration_seconds: duración del viaje en segundos
