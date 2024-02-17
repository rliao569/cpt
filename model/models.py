# models.py

from __init__ import db

class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(255), nullable=False)

    def __repr__(self):
        return f"<Comment {self.id}>"

