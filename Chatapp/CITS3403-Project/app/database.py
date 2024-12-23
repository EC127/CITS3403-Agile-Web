# database operation functions

from app import db
from app.models import User, Chat, Message, BotResponse
from datetime import datetime


def register_user(username, password):
    new_user = User(username=username, created_at=datetime.now())
    new_user.set_password(password)

    db.session.add(new_user)
    db.session.commit()

    user_id = new_user.user_id
    return user_id


def create_chat(user_id):
    # Check if there exist a chat of current user
    existing_chat = Chat.query.filter_by(user_id=user_id).first()

    if existing_chat:
        # if the chat exist, return the chat_id of the chat
        chat_id = existing_chat.chat_id
        return chat_id
    else:
        # If the chat not exist, create one, and return the id.
        new_chat = Chat(user_id=user_id, created_at=datetime.now())

        db.session.add(new_chat)
        db.session.commit()

        chat_id = new_chat.chat_id
        return chat_id


def save_message(chat_id, user_id, content, timestamp):
    user_message = Message(chat_id=chat_id, user_id=user_id,
                           content=content, timestamp=timestamp)

    db.session.add(user_message)
    db.session.commit()

    message_id = user_message.message_id
    return message_id


def save_response(message_id, content, timestamp):
    new_response = BotResponse(
        message_id=message_id, content=content, timestamp=timestamp)

    db.session.add(new_response)
    db.session.commit()

    response_id = new_response.response_id
    return response_id


def save_chat_message(user_id, user_message, message_timestamp, bot_reply, response_timestamp):

    # try to create the chat
    chat_id = create_chat(user_id)

    # create a new message
    message_id = save_message(
        chat_id, user_id, user_message, message_timestamp)

    # create a bot response
    save_response(message_id, bot_reply, response_timestamp)
