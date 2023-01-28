#!/usr/bin/env bash
# exit on error
echo "Building the project"

set -o errexit

pip install -r requirements.txt

python manage.py collectstatic --no-input
python manage.py migrate

echo "Starting the server"