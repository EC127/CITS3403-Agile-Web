from app import Config
import openai

openai.api_key = Config.OPENAI_API_KEY


def get_chat_response(user_message, chat_history=None):
    if chat_history is None:  # check if it is the first conversation
        chat_history = [
            {'role': 'system', 'content': 'You are a chatbot, introduce what you can do to the user.'}]

    chat_history.append({'role': 'user', 'content': user_message})

    response = openai.ChatCompletion.create(
        model='gpt-3.5-turbo',
        messages=chat_history
    )

    bot_reply = response['choices'][0]['message']['content']

    return bot_reply, chat_history
