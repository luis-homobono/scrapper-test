# CODIGO DE PRUEBA TECNICA

Código de API de scrapper y para formatear un JSON a CSV.

Cada una de las pruebas esta en una carpeta determinada, son sus respectivos archivos de requirements.txt

## Instalación API
Sí tu deseas instalar la api en tu local puedes hacer uso de los siguientes compandos:
1. Creación de ambiente virtual
```{bash}
python -m venv venv
source venv/bin/activate
```
2. Instalación de librerias
```{bash}
pip install -r requirements.txt
```
3. Correr pruebas unitarias (NO IMPLEMENTADO) # TODO: Necesita pruebas unitarias
```{bash}
pytest --verbosity=2
```
4. Correr el servidor:
```{bash}
flask run
```

Sí deseas revisar la documentación de la API con Swagger-UI puedes revisarlo en la siguiente liga: [http://localhost:5000/swagger-ui](http://localhost:5000/swagger-ui)


## Instalación API con DOCKER
Sí tu deseas instalar la api en tu local puedes hacer uso de los siguientes compandos:
1. Creación de imagen de docker
```{bash}
docker build -f Dockerfile -t selenium_test .
```
2. Instalación de librerias
```{bash}
docker run --name relenium -p 5001:5000 -v ${PWD}:/var/www/ -it selenium_test:latest
```
