import string
import random

def random_email():
    letters = string.ascii_lowercase
    username = ''.join(random.choice(letters) for _ in range(10))
    domain = ''.join(random.choice(letters) for _ in range(5))
    return f"{username}@{domain}.com"


