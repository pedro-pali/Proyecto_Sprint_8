import pandas as pd
import requests 
from bs4 import BeautifulSoup

# Gurdamos la URL de donde obtendremos los datos en la variable url.
url = 'https://practicum-content.s3.us-west-1.amazonaws.com/data-analyst-eng/moved_chicago_weather_2017.html'
# Utilizamos la librería request para obtener los datos de la URL y los almacenamos en la variable req.
req = requests.get(url)
# Utilizamos la librería BeautifulSoup para ordenar los datos en estructura de árbol.
soup = BeautifulSoup(req.text, 'lxml')

# Almacenamos en la variable table los datos estructurados con las condiciones dadas,
# utilizando find(), le decimos que busque sobre los atributos señalados en las llaves.
table = soup.find('table', attrs={"id": "weather_records"})

# Almacenamos los nombres de las columnas en la lista weather_columns,
# guardamos los nombres de las columnnas ('th') en la variable headers y
# extraemos solo el texto con .text y un bucle for.
weather_columns = []
headers = table.find_all('th')
for head in headers:
    weather_columns.append(head.text)

# Almacenamos los datos de la tabla en la lista vacia weather_rows,
# guardamos en la variable body con el método find_all() todos los datos de las filas ('tr'),
# recorremos los datos de las filas y paramos en cada una de las celdas ('td'), 
# si no es celda se lo brinca, esto para saltar el encabezado,
# creamos una variable para extraer el texto de cada celda y limpiar los espacios,
# guardamos los resultados en la lista de weather_rows.
weather_rows = []
body = table.find_all('tr')
for row in body:
    cells = row.find_all('td')
    if not cells:
        continue
    values = [cell.get_text(strip=True) for cell in cells]
    weather_rows.append(values)

# Creamos el DF weather_records
weather_records = (pd.DataFrame(weather_rows, columns = weather_columns))
print(weather_records)