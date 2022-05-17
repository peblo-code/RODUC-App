# Bienvenido a RODUC-APP!

Hola!, este es un proyecto para la **Universidad Católica**. Y aquí te dejare instrucciones de como correr los proyectos. Por un lado tenemos a **Django** como framework Web y servidor de API, además **React Native** como framework de aplicación móvil.

# Como correr React Native
 1. Debes descargar [Node.js](https://nodejs.org/es/), la versión LTS
    para ser específicos.
 2. Ejecuta tu terminal en **Administrador**, debes posicionarte en el directorio de *"~/RODUC-App"*
 3. Dentro del directorio *"~/RODUC-App"* escribes:
> npm install --global expo-cli

Este comando instalará **Expo** en tu computadora, una plataforma que trabajará en conjunto con *React Native*. Mas info sobre [expo.dev](https://expo.dev/)

 4. Luego, para instalar las dependencias del proyecto ejecutas:
> npm i

5. Y listo!, para iniciar el proyecto escribes:

> npm start

  
# Como correr Django

 1. Descargar [Python.](https://www.python.org/downloads/)
 2. Con tu terminal, ingresas a *"~/RODUC-App/RoducApp"*.
 3. Instalas el framework **Django**: 

> pip install django

 4. Instalas las dependencias del proyecto de **Django** con:
> pip install -r requirements.txt

5. Configuras la conexión a base de datos del archivo *settings.py* en el directorio *"~/RODUC-App/RoducApp/RoducApp"*

    `DATABASES  = {
    	'default': {
    	'ENGINE': 'django.db.backends.mysql',
    	'NAME': 'roducdb',
    	'USER' : 'usuario',
    	'PASSWORD': 'contraseña',
    	'HOST' : 'ip-de-host',
    	'PORT' : '3306',
    }}`

6. Inicias el servidor, regresando al directorio anterior

> python manage.py runserver
