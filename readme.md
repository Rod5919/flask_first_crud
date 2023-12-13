# Primera aplicación con Flask

## Paso 1: Crear un entorno virtual

```bash
# Download https://bootstrap.pypa.io/get-pip.py
python3 get-pip.py
pip3 install virtualenv # python3 -m pip install virtualenv
python3 -m venv venv
```

## Paso 2: Activar el entorno virtual

```bash
# Linux
source venv/bin/activate

# Windows
venv\Scripts\activate
```

## Paso 3: Instalar dependencias

```bash
pip3 install -r requirements.txt # o python3 -m pip install -r requirements.txt
```

## Paso 4: Crear el arbol de directorios

```bash
|-- .env
|-- .gitignore
|-- app.py
|-- requirements.txt
`-- config
    `-- config.py
`-- controllers
    `-- user_controller.py
`-- db
    `-- db.py
`-- models
    |-- __init__.py
    `-- user_model.py
|-- readme.md
|-- requirements.txt
`-- routes
    |-- __init__.py
    |-- html_routes.py
    |-- main_routes.py
    `-- user_routes.py
`-- templates
    `-- index.html
`-- utils
    |-- __init__.py
    `-- encryptor.py
```

## Paso 5: Crear archivo app.py

El archivo `app.py` es el encargado de ejecutar la aplicación.

## Paso 6: Crear archivo de configuración config.py

El archivo `config.py` es el encargado de configurar la aplicación y archivo `.env`, este archivo no debe ser subido al repositorio.

## Paso 7: Crear base de datos

La base de datos se crea en railway, para ello se debe crear una cuenta en [railway](https://railway.app/), luego se debe crear un nuevo proyecto y por último se debe crear una base de datos postgresql.

## Paso 8: Crear archivo db.py

El archivo `db.py` es el encargado de crear la conexión con la base de datos.

## Paso 9: Crear archivo user_model.py

El archivo `user_model.py` es el encargado de crear el modelo de usuario.

## Paso 10: Crear rutas

Las rutas son las encargadas de recibir las peticiones del cliente y enviar una respuesta.

## Paso 11: Crear archivo user_controller.py

El archivo `user_controller.py` es el encargado de recibir las peticiones del cliente y enviar una respuesta.

## Paso 12: Crear archivo index.html

El archivo `index.html` es el encargado de mostrar la vista principal de la aplicación.

## Paso 13: Crear archivo encryptor.py

El archivo `encryptor.py` es el encargado de encriptar y desencriptar contraseñas.

## Paso 14: Ejecutar la aplicación

### Forma 1

```bash
python app.py
```

### Forma 2

```bash

```bash
flask run
```
