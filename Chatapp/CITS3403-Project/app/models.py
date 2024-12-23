# defining database models

from app import db
# from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

# User Table


class User(db.Model):        # it was class User(UserMixin,db.Model):
    user_id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50))
    password = db.Column(db.String(50))
    created_at = db.Column(db.TIMESTAMP)

    def __repr__(self):
        return '<User {} with name {}>'.format(self.user_id, self.username)

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)

# Chat Table


class Chat(db.Model):
    chat_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.user_id'))
    created_at = db.Column(db.TIMESTAMP)
    user = db.relationship('User', backref=db.backref('chats', lazy=True))

    def __repr__(self):
        return '<Chat {} created at {}>'.format(self.chat_id, self.created_at)

# Message Table


class Message(db.Model):
    message_id = db.Column(db.Integer, primary_key=True)
    chat_id = db.Column(db.Integer, db.ForeignKey('chat.chat_id'))
    user_id = db.Column(db.Integer, db.ForeignKey('user.user_id'))
    content = db.Column(db.Text)
    timestamp = db.Column(db.TIMESTAMP)
    chat = db.relationship('Chat', backref=db.backref('messages', lazy=True))
    user = db.relationship('User', backref=db.backref('messages', lazy=True))

    def __repr__(self):
        return '<Message {} at {}>'.format(self.message_id, self.timestamp)

# BotResponse Table


class BotResponse(db.Model):
    response_id = db.Column(db.Integer, primary_key=True)
    message_id = db.Column(db.Integer, db.ForeignKey('message.message_id'))
    content = db.Column(db.Text)
    timestamp = db.Column(db.TIMESTAMP)
    message = db.relationship(
        'Message', backref=db.backref('bot_responses', lazy=True))

    def __repr__(self):
        return '<BotResponse {} at {}>'.format(self.response_id, self.timestamp)
