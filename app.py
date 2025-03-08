from flask import Flask, jsonify, request
from flask_migrate import Migrate
from flask_cors import CORS
from models import db, TodoItem
from config import Config

# Initialize the Flask app
app = Flask(__name__)

# Load the configuration from config.py
app.config.from_object(Config)
CORS(app)  # Enable CORS

# Initialize the database with the app
db.init_app(app)

# Initialize Flask-Migrate with the app and db
migrate = Migrate(app, db)


@app.route('/')
def home():
    return "Hello, Flask!"

@app.route('/todos', methods=['GET'])
def get_todos():
    todos = TodoItem.query.all()
    return jsonify([{'id': todo.id, 'task': todo.task, 'completed': todo.completed} for todo in todos])

@app.route('/todos', methods=['POST'])
def add_todo():
    data = request.get_json()
    new_todo = TodoItem(task=data['task'])
    db.session.add(new_todo)
    db.session.commit()
    return jsonify({'id': new_todo.id, 'task': new_todo.task, 'completed': new_todo.completed}), 201

@app.route('/todos/<int:id>', methods=['PUT'])
def update_todo(id):
    todo = TodoItem.query.get(id)
    if todo:
        data = request.get_json()
        todo.completed = data['completed']
        db.session.commit()
        return jsonify({'id': todo.id, 'task': todo.task, 'completed': todo.completed})
    return jsonify({'message': 'Todo not found'}), 404

@app.route('/todos/<int:id>', methods=['DELETE'])
def delete_todo(id):
    todo = TodoItem.query.get(id)
    if todo:
        db.session.delete(todo)
        db.session.commit()
        return jsonify({'message': 'Todo deleted'})
    return jsonify({'message': 'Todo not found'}), 404

@app.route("/health")
def health():
    return "OK", 200  # Liveness Probe. we used this in k8s deployment

@app.route("/ready")
def ready():
    return "Ready", 200  # Readiness Probe. we used this in k8s deployment


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)

