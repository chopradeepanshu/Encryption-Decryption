from src import Utils


class Encryption:
    def __init__(self):
        pass

    @staticmethod
    def encrypt(message):
        encrypted_message = message
        for c in message:
            if c in Utils.keys():
                encrypted_message = encrypted_message.replace(c, Utils.keys().get(c))
        return encrypted_message
