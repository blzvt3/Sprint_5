import random

class Generator:
    @staticmethod
    def generate_email():
        return f"art{random.randint(1, 9999)}@yandex.ru"

    @staticmethod
    def generate_valid_password():
        return f"pass{random.randint(10000, 99999)}"

    @staticmethod
    def generate_invalid_password():
        return f"p{random.randint(100, 999)}"