import random
import string


class CommonApiHelper:
    def generate_random_string(self, length=10):
        letters = string.ascii_lowercase
        random_string = "".join(random.choice(letters) for i in range(length))
        return random_string
