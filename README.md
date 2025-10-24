# py-78130-alvarez
Repositorio del proyecto final para el curso de Python Flex, comisión 78130.

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

