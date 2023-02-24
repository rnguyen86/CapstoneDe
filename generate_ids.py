import random
import string


def generate_ids():

    uid = ''.join(random.choices(string.ascii_uppercase + string.digits, k=10))
    return uid

