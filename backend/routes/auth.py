from flask import request, jsonify
from .. import app, db, bcrypt, jwt, User
from ..utils import password_checker
from flask_jwt_extended import create_access_token, jwt_required
from werkzeug.utils import secure_filename
import os


@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()

    if 'username' not in data or not data['username']:
        return jsonify({'message': 'Username is required.'}), 400
    if 'password' not in data or not data['password']:
        return jsonify({'message': 'Password is required.'}), 400

    password_error = password_checker(data['password'])
    if password_error is not None:
        return jsonify({'message': password_error}), 400
    
    existing_user = User.query.filter_by(username=data['username']).first()
    if existing_user is not None:
        return jsonify({'message': 'Username already taken.'}), 400

    hashed_password = bcrypt.generate_password_hash(data['password']).decode('utf-8')
    new_user = User(username=data['username'], password=hashed_password)
    db.session.add(new_user)
    db.session.commit()
    return jsonify({'message': 'User registered successfully!'})

@app.route('/login', methods=['POST'])
def login():
    if not request.is_json:
        return jsonify({"message": "Missing JSON in request"}), 400

    data = request.get_json()

    if 'username' not in data or not data['username']:
        return jsonify({'message': 'Username is required.'}), 400
    if 'password' not in data or not data['password']:
        return jsonify({'message': 'Password is required.'}), 400

    user = User.query.filter_by(username=data['username']).first()

    if user and bcrypt.check_password_hash(user.password, data['password']):
        access_token = create_access_token(identity=user.id)
        return jsonify({'access_token': access_token}), 200

    return jsonify({'message': 'Invalid username or password'}), 400


@app.route('/logout', methods=['POST'])
@jwt_required()  # Requires a valid access token
def logout():
    return jsonify({'message': 'Logout successful'})