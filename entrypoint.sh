#!/bin/sh

set -e  # Exit immediately if any command fails

echo "Running migrations..."
flask db init
flask db migrate -m "inial"
flask db upgrade  # No need for init/migrate every time

echo "Starting application..."
exec python /app/app.py  # Use exec to replace shell with Python process