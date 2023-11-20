from datetime import datetime
from flask import request, jsonify
from .. import app, db, Todo
from ..utils import todo_to_dict
from flask_jwt_extended import jwt_required, get_jwt_identity
from dateutil.parser import parse


@app.route('/todos', methods=['GET'])
@jwt_required()
def get_todos():
    current_user = get_jwt_identity()
    sorting_order = request.args.get('sort', default='createdAt', type=str)

    if sorting_order == 'createdAt':
        todos = Todo.query.filter_by(user_id=current_user).order_by(Todo.createdAt.desc()).all()
    elif sorting_order == '-createdAt':
        todos = Todo.query.filter_by(user_id=current_user).order_by(Todo.createdAt).all()
    elif sorting_order == 'task':
        todos = Todo.query.filter_by(user_id=current_user).order_by(Todo.task).all()
    elif sorting_order == '-task':
        todos = Todo.query.filter_by(user_id=current_user).order_by(Todo.task.desc()).all()
    elif sorting_order == 'priority':
        todos = Todo.query.filter_by(user_id=current_user).order_by(Todo.priority).all()
    elif sorting_order == '-priority':
        todos = Todo.query.filter_by(user_id=current_user).order_by(Todo.priority.desc()).all()
    elif sorting_order == 'due_date':
        todos = Todo.query.filter_by(user_id=current_user).order_by(Todo.due_date).all()
    elif sorting_order == '-due_date':
        todos = Todo.query.filter_by(user_id=current_user).order_by(Todo.due_date.desc()).all()
    elif sorting_order == 'category':
        todos = Todo.query.filter_by(user_id=current_user).order_by(Todo.category_id).all()
    else:
        todos = Todo.query.filter_by(user_id=current_user).all()

    return jsonify([todo_to_dict(todo) for todo in todos])




@app.route('/todos', methods=['POST'])
@jwt_required()
def add_todo():
    current_user = get_jwt_identity()
    data = request.get_json()

    if 'task' not in data or not data['task']:
        return jsonify({'message': 'Task is required'}), 400

    if 'priority' not in data or not 1 <= data['priority'] <= 3:
        return jsonify({'message': 'Priority is required and should be between 1 and 3'}), 400

    if 'due_date' not in data:
        due_date = None
    else:
        due_date = parse(data['due_date'])
    category_id = data.get('category_id')
    if not category_id:
        category_id = None

    new_todo = Todo(task=data['task'], user_id=current_user, priority=data['priority'], due_date=due_date, category_id=category_id)
    db.session.add(new_todo)
    db.session.commit()
    return jsonify({'message': 'Todo added successfully!'})



@app.route('/todos/<int:todo_id>', methods=['DELETE'])
@jwt_required()
def delete_todo(todo_id):
    current_user = get_jwt_identity()
    todo = Todo.query.get(todo_id)
    if todo is None:
        return jsonify({'message': 'Todo does not exist'}), 404
    if todo.user_id != current_user:
        return jsonify({'message': 'Not authorized'}), 401
    db.session.delete(todo)
    db.session.commit()
    return jsonify({'message': 'Todo deleted successfully'})


@app.route('/todos/<int:todo_id>', methods=['PUT'])
@jwt_required()
def update_todo(todo_id):
    current_user = get_jwt_identity()
    data = request.get_json()

    if 'task' not in data or not data['task']:
        return jsonify({'message': 'Task is required'}), 400
    if 'completed' not in data:
        return jsonify({'message': 'Completed status is required'}), 400
    if 'priority' not in data or not 1 <= data['priority'] <= 3:
        return jsonify({'message': 'Priority is required and should be between 1 and 3'}), 400
    if 'due_date' not in data or not data['due_date']:
        due_date = None
    else:
        due_date = parse(data['due_date'])
    category_id = data.get('category_id')
    if not category_id:
        category_id = None

    todo = Todo.query.get(todo_id)
    if todo is None:
        return jsonify({'message': 'Todo does not exist'}), 404
    if todo.user_id != current_user:
        return jsonify({'message': 'Not authorized'}), 401

    todo.task = data['task']
    todo.completed = data['completed']
    todo.priority = data['priority']
    todo.due_date = due_date
    todo.category_id = category_id
    db.session.commit()
    return jsonify({'message': 'Todo updated successfully'})


