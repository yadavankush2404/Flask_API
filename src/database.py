from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import string,random
from enum import unique
from sqlalchemy.orm import backref

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    username = db.Column(db.String(80),unique =True,nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.Text,nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, onupdate=datetime.utcnow)
    bookmarks = db.relationship('Bookmark',backref="user")

    def __repr__(self) -> str:
        return f'User >>> {self.username}'
    
class Bookmark(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    body = db.Column(db.Text, nullable=True)
    url = db.Column(db.Text,nullable=False)
    short_url = db.Column(db.String(3),nullable=True)
    visits = db.Column(db.Integer, default=0)
    user_id = db.Column(db.Integer,db.ForeignKey('user.id'))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, onupdate=datetime.utcnow)

    def generate_short_characters(self):
        characters = string.digits+string.ascii_letters # from the string contaning all possible characters allowed digits and ascii
        picked_chars =  ''.join(random.choices(characters,k=3)) # random.choices returns a list of k randomly picked characters.
        
        link = self.query.filter_by(short_url=picked_chars).first() # making sure the three picked chars are not pre-existing.

        if link:
            return self.generate_short_characters()
        else:
            return picked_chars
        

    def __init__(self,**kwargs):
        super().__init__(**kwargs)

        self.short_url= self.generate_short_characters() # method inside constructor to assign short_url for every url entry made

    def __repr__(self) -> str:
        return f'Bookmark >>> {self.url} {self.body}'

    

