import random

def handle_response(message) -> str:
    p_message = message.lower()
    if p_message == 'hello':
        return 'Hey there!'

    if p_message == 'roll':
        return 'no'

    if p_message == 'help':
        return "helping"

    if user_message[0:8] == '!register':
            user_message = user_message[9:]
            name = user_message
    return f"something something {name}"