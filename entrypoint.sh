#!/bin/bash

# Salir si hay errores
set -e

# Migraciones
echo "Ejecutando migraciones..."
python manage.py migrate --noinput

# Recolección de estáticos
echo "Recolectando archivos estáticos..."
python manage.py collectstatic --noinput

# Iniciar servidor Gunicorn
echo "Iniciando servidor Gunicorn..."
exec gunicorn config.wsgi:application --bind 0.0.0.0:8000 --workers 3
