from src import Utils


class Decryption:
    def __init__(self):
        pass

    @staticmethod
    def decrypt(message):
        decrypted_message = message
        keys_values = Utils.keys().values()
        for c in message:
            if c in keys_values:
                decrypted_message = decrypted_message.replace(c, Decryption.get_key(c))
        return decrypted_message

    def get_key(val):
        for key, value in Utils.keys().items():
            if val == value:
                return key
