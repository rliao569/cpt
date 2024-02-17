import json, jwt
from flask import Blueprint, request, jsonify,  make_response, Response, current_app
from flask_restful import Api, Resource # used for REST API building
from flask_login import login_user, logout_user, current_user, login_required
from werkzeug.security import check_password_hash
from flask_cors import CORS
from auth_middleware import token_required
from werkzeug.security import generate_password_hash
from datetime import datetime
from model.users import User
from __init__ import db, app
from model.models import Comment
comments_api = Blueprint('comments_api', __name__, url_prefix='/api/comments')
api = Api(comments_api)
# Initialize the SQLAlchemy object to work with the Flask app instance
db.init_app(app)

class CommentAPI:
    class CRUD(Resource):
       # @token_required
        def get(self, current_user):
            try:
                # Fetch comments from the database
                comments = Comment.query.all()
                # Convert comments to JSON-ready format
                json_ready = [{'id': comment.id, 'text': comment.text} for comment in comments]
                return jsonify(json_ready), 200
            except Exception as e:
                return {'message': 'Failed to fetch comments', 'error': str(e)}, 500
        @token_required
        def post(self, current_user):
            try:
                data = request.get_json()
                text = data.get('text')
                if not text:
                    return {'message': 'Text is required for comment'}, 400
                new_comment = Comment(text=text)
                db.session.add(new_comment)
                db.session.commit()
                return {'message': 'Comment submitted successfully'}, 201
            except Exception as e:
                return {'message': 'Failed to submit comment', 'error': str(e)}, 500
                
    api.add_resource(CRUD, '/')