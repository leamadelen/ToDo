import re
from flask import current_app
import os

def password_checker(password):
    if len(password) < 8:
        return 'Password must be at least 8 characters.'
    if not re.search('[A-Z]', password):
        return 'Password must contain at least one uppercase letter.'
    if not re.search('[a-z]', password):
        return 'Password must contain at least one lowercase letter.'
    if not re.search('[0-9]', password):
        return 'Password must contain at least one digit.'
    return None

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in current_app.config['ALLOWED_EXTENSIONS']

def todo_to_dict(todo):
    return {
        'id': todo.id,
        'task': todo.task,
        'completed': todo.completed,
        'priority': todo.priority,
        'due_date': todo.due_date.strftime("%Y-%m-%d %H:%M:%S") if todo.due_date else None,
        'category_id': todo.category_id
    }

def category_to_dict(category):
    return {
        'id': category.id,
        'name': category.name,
        'user_id': category.user_id
    }