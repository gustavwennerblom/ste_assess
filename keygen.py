import random


def get_secret_key(length):
    """
    :param length: Length of key
    :return: A randomized secret key for the app
    """
    allowed_chars = 'abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(-_=+)'
    secret_key = ''.join(random.choice(allowed_chars) for i in range(length))
    print("Secret key is: {}".format(secret_key))
    return secret_key
