from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Dummy data for demonstration
comments = [
    {"restaurantName": "Restaurant 1", "rating": 8},
    {"restaurantName": "Restaurant 2", "rating": 7},
    # Add more comments as needed
]

# Route to fetch comments
@app.route('/api/comments', methods=['GET'])
def get_comments():
    return jsonify(comments)

# Route to submit a new comment
@app.route('/api/comments', methods=['POST'])
def submit_comment():
    data = request.json
    # Your logic to handle comment submission
    # For demonstration, just append the comment to the list
    comments.append(data)
    return jsonify({"message": "Comment submitted successfully"}), 201

if __name__ == '__main__':
    app.run(port=8888)  # Run the Flask app on port 8888
