#!/bin/sh

set -e  # Exit immediately if any command fails

# echo "Running migrations..."
# if [ ! -d "migrations" ]; then
#   flask db init
#   flask db migrate -m "inial"
#   flask db upgrade
# fi


echo "Starting application..."
exec python /app/app.py 