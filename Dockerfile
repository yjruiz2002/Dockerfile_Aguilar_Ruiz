# Utilizamos la imagen base de Python 3.9
FROM python:3.9

# Establecemos el directorio de trabajo dentro del contenedor como /app
WORKDIR /app

# Copiamos el archivo requirements.txt al directorio de trabajo
COPY requirements.txt ./

# Instalamos las dependencias definidas en requirements.txt
RUN pip install -r requirements.txt

# Copiamos el contenido actual del directorio de construcción al directorio de trabajo en el contenedor
COPY . .

# Exponemos el puerto 5000 para que pueda ser accesible desde fuera del contenedor
EXPOSE 5000

# Definimos el comando que se ejecutará cuando se inicie el contenedor
CMD [ "flask", "run", "--host=0.0.0.0", "--port=4000"]