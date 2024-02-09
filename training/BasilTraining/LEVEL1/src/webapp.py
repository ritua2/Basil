from flask import Flask, jsonify, request, render_template
import os

app = Flask(__name__)

# Sample data - Todo list
todo_list = [
    {"id": 1, "task": "Finish homework", "completed": False},
    {"id": 2, "task": "Buy groceries", "completed": True},
    {"id": 3, "task": "Go for a run", "completed": False}
]
@app.route('/', methods=['GET'])
def home():
    # HTML for todo app home page
    return render_template('home.html')


# API to get all todos
@app.route('/todos', methods=['GET'])
def get_todos():
    return jsonify(todo_list)

# API to get a specific todo by ID
@app.route('/todos/<int:todo_id>', methods=['GET'])
def get_todo(todo_id):
    todo = next((item for item in todo_list if item["id"] == todo_id), None)
    if todo:
        return jsonify(todo)
    else:
        return jsonify({"error": "Todo not found"}), 404

# API to create a new todo
@app.route('/todos', methods=['POST'])
def create_todo():
    data = request.get_json()
    new_todo = {
        "id": len(todo_list) + 1,
        "task": data.get("task"),
        "completed": False
    }
    todo_list.append(new_todo)
    return jsonify(new_todo), 201

# API to update a todo by ID
@app.route('/todos/<int:todo_id>', methods=['PUT'])
def update_todo(todo_id):
    todo = next((item for item in todo_list if item["id"] == todo_id), None)
    if not todo:
        return jsonify({"error": "Todo not found"}), 404
    data = request.get_json()
    todo.update(data)
    return jsonify(todo)

# API to delete a todo by ID
@app.route('/todos/<int:todo_id>', methods=['DELETE'])
def delete_todo(todo_id):
    global todo_list
    todo_list = [item for item in todo_list if item["id"] != todo_id]
    return '', 204

if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True)
