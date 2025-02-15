python3 -m venv env

source env/bin/activate

# Run if requirements.txt file doesn't work
pip install Flask  flask-cors
pip install psycopg2-binary
pip install flask-sqlalchemy
pip install python-dotenv
pip install Flask-SQLAlchemy Flask-Migrate

# For DB migrations
flask db init
flask db migrate -m "Initial migration after resetting"
flask db upgrade

# Install supervisor and gunicorn
sudo apt install supervisor -y
pip install gunicorn

Since your command is flask run, you need to run it with Gunicorn:

$ gunicorn -w 4 -b 0.0.0.0:5000 "app:app"

$ sudo nano /etc/supervisor/conf.d/flask_app.conf
<<
[program:flask_app]
command=/var/www/project/venv/bin/gunicorn -w 4 -b 0.0.0.0:8000 "app:app"
directory=/var/www/project/your_flask_project
autostart=true
autorestart=true
stderr_logfile=/var/log/flask_app.err.log
stdout_logfile=/var/log/flask_app.out.log
user=youruser
>>
