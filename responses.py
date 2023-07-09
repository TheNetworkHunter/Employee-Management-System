import random

def response_handler(message) -> str:
    p_message = message.lower()

    if p_message == 'hello':
        return str(random.randint(1.6))