# py-78130-alvarez
Repositorio del proyecto final para el curso de Python Flex, comisión 78130. Se trata de una aplicación de E-commerce de venta de álbumes donde los usuarios pueden crear sus perfiles para recibir información sobre cualquier nuevo producto que ingresa. 

# Instalación y puesta en marcha

## Clonar el repositorio

bash
git clone [URL](https://github.com/rocialvarez/py-78130-alvarez.git)
cd pythonfinal

## Crear Entorno Virtual

python -m venv env

## Activar Entorno
Windows: env\Scripts\activate
Mac/Linux: source env/bin/activate

## Instalar Dependencias
pip install -r requirements.txt

## Aplicar migraciones

python manage.py makemigrations
python manage.py migrate

## Ejecturar Servidor
python manage.py runserver

