from app import db
from datetime import datetime
from flask import url_for

class Movie(db.Model):
    __tablename__ = 'movies'
    
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), nullable=False)
    description = db.Column(db.String(1000), nullable=False)
    poster = db.Column(db.String(200), nullable=False)  
    created_at = db.Column(db.DateTime, nullable=False)
    
    def __init__(self, title, description, poster):
        self.title = title
        self.description = description
        self.poster = poster
        self.created_at = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    def serialize(self):
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'poster': url_for('getImage', filename = self.poster),
        }
        
    def __repr__(self):
        return f'<Movie {self.title}>'