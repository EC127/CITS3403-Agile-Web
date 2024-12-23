#  defining routes and view functions

from flask import render_template, request, redirect, url_for, session, jsonify
from datetime import datetime

from app import app, db
from app.models import User, Chat, Message, BotResponse
from app.database import register_user, create_chat, save_message, save_response, save_chat_message
from app.bot import get_chat_response

# Global variable
user_messages = []
timestamps = []
chat_history = []

# Login route and view function


@app.route('/')
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        # Validate user credentials
        user = User.query.filter(User.username == username).first()
        if user and user.check_password(password):
            session['username'] = user.username  # store user name into session
            session['user_id'] = user.user_id  # store user id into session
            response_data = {'success': True, 'username': user.username}
        else:
            response_data = {'invalid': True}
        return jsonify(response_data)

    return render_template('views/login.html')


# Validate user credentials
@app.route('/chat', methods=['GET', 'POST'])
def chat():
    global chat_history
    if 'username' in session:
        current_user_id = session.get('user_id')
        if request.method == 'POST':
            # Timestamp of user message
            message_timestamp = datetime.now()

            # Validate user credentials
            while timestamps and (message_timestamp - timestamps[0]).total_seconds() >= 60:
                user_messages.pop(0)
                timestamps.pop(0)
            # Check if the number of user messages exceeds the limit
            if len(user_messages) >= 3:
                # Return an error message
                return jsonify({'error': 'Spamming'}
                               )
            user_message = request.json['message']
            user_messages.append(user_message)
            timestamps.append(message_timestamp)

            # Call the get_chat_response function and pass the chat history
            response, chat_history = get_chat_response(
                user_message, chat_history)

            # Timestamp of bot reply
            response_timestamp = datetime.now()

            # Save to database
            if chat_history:
                user_id = current_user_id
                save_chat_message(
                    user_id, user_message, message_timestamp, response, response_timestamp)

            # Return the response from GPT to the frontend
            return jsonify({'response': response})

        return render_template('views/chat.html')
    else:
        return redirect(url_for('login'))

# Search route and view function


@app.route('/search', methods=['GET', 'POST'])
def search():
    if 'username' in session:
        current_user_id = session.get('user_id')

        if request.method == 'POST':
            keyword = request.json.get('query')
            # Filter messages and bot responses using the current user's ID
            messages = Message.query.join(Chat).filter(
                Message.content.contains(keyword),
                Chat.user_id == current_user_id
            ).all()

            bot_responses = BotResponse.query.join(Message).join(Chat).filter(
                BotResponse.content.contains(keyword),
                Message.chat_id == Chat.chat_id,
                Chat.user_id == current_user_id
            ).all()

            message_results = [
                {
                    'content': message.content,
                    'type': 'message',
                    'timestamp': message.timestamp,
                    'sender': message.user.username
                }
                for message in messages
            ]

            bot_response_results = [
                {
                    'content': response.content,
                    'type': 'bot_response',
                    'timestamp': response.timestamp,
                    'sender': 'Bot'
                }
                for response in bot_responses
            ]

            results = message_results + bot_response_results

            # Sort by absolute timestamp in ascending order
            results = sorted(results, key=lambda x: x['timestamp'])

            return jsonify({'results': results})
        return render_template('views/search.html')
    else:
        return redirect(url_for('login'))

# Register route and view function


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        # Check if the username already exists
        existing_user = User.query.filter(User.username == username).first()
        if existing_user:
            return jsonify({'exist': True})
        else:
            # Create a new user
            register_user(username, password)

            return jsonify({'success': True})

    return render_template('views/register.html')


# Logout route and view function
@app.route('/logout')
def logout():
    session.clear()  # Clear the current user from the session
    return redirect(url_for('login'))
