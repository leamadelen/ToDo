from flask import request, jsonify
from .. import app, db, Category
from ..utils import category_to_dict
from flask_jwt_extended import jwt_required, get_jwt_identity

@app.route('/categories', methods=['POST'])
@jwt_required()
def create_category():
    current_user = get_jwt_identity()
    data = request.get_json()

    if 'name' not in data or not data['name']:
        return jsonify({'message': 'Name is required'}), 400

    category = Category(name=data['name'], user_id=current_user)
    db.session.add(category)
    db.session.commit()
    return jsonify(category_to_dict(category)), 201

@app.route('/categories', methods=['GET'])
@jwt_required()
def get_categories():
    current_user = get_jwt_identity()
    categories = Category.query.filter_by(user_id=current_user).all()
    return jsonify([category_to_dict(category) for category in categories])

@app.route('/categories/<int:category_id>', methods=['GET'])
@jwt_required()
def get_category(category_id):
    current_user = get_jwt_identity()
    category = Category.query.get(category_id)

    if category is None or category.user_id != current_user:
        return jsonify({'message': 'Category does not exist or you do not have permission to view it'}), 404

    return jsonify(category_to_dict(category))

@app.route('/categories/<int:category_id>', methods=['PUT'])
@jwt_required()
def update_category(category_id):
    current_user = get_jwt_identity()
    data = request.get_json()

    if 'name' not in data or not data['name']:
        return jsonify({'message': 'Name is required'}), 400

    category = Category.query.get(category_id)
    if category is None or category.user_id != current_user:
        return jsonify({'message': 'Category does not exist or you do not have permission to update it'}), 404

    category.name = data['name']
    db.session.commit()
    return jsonify(category_to_dict(category))

@app.route('/categories/<int:category_id>', methods=['DELETE'])
@jwt_required()
def delete_category(category_id):
    current_user = get_jwt_identity()
    category = Category.query.get(category_id)

    if category is None or category.user_id != current_user:
        return jsonify({'message': 'Category does not exist or you do not have permission to delete it'}), 404

    db.session.delete(category)
    db.session.commit()
    return jsonify({'message': 'Category deleted successfully'})
