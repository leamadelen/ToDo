from flask import request, jsonify, send_from_directory, current_app
from .. import app, db, User
from ..utils import allowed_file
from flask_jwt_extended import jwt_required, get_jwt_identity
from werkzeug.utils import secure_filename
import os


@app.route('/upload_profile_pic', methods=['POST'])
@jwt_required()
def upload_profile_pic():
    current_user_id = get_jwt_identity()
    current_user = User.query.get(current_user_id)
    
    if 'file' not in request.files:
        return jsonify({"error": "No file part"}), 400
    file = request.files['file']
    if file.filename == '':
        return jsonify({"error": "No selected file"}), 400
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file_path = os.path.join(current_app.config['UPLOAD_FOLDER'], filename)
        file.save(file_path)

        current_user.profile_picture = filename  # Only store the filename and extension
        db.session.commit()

        return jsonify({"message": "Profile picture updated successfully"}), 200
    else:
        return jsonify({"error": "Invalid file type"}), 400

@app.route('/profile', methods=['GET'])
@jwt_required()
def get_profile():
    current_user_id = get_jwt_identity()
    current_user = User.query.get(current_user_id)

    return jsonify({
        "username": current_user.username,
        "profile_picture": current_user.profile_picture
    })

@app.route('/profilepics/<filename>')
def serve_profile_pic(filename):
    return send_from_directory(current_app.config['UPLOAD_FOLDER'], filename)