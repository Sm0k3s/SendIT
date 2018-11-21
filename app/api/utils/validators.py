import re


class Validators():
    """class to check validity of inputs"""
    @staticmethod
    def check_email(email):
        if re.match(r"[\w]+[\d]?@[\w]+\.[\w]+", email):
            return True

    @staticmethod
    def check_username(username):
        if re.match(r"[^\W][A-Za-z]?[\w]?[-_]?[A-Za-z0-9]{2,}", username):
            return True

    @staticmethod
    def check_password(password):
        if re.match(r"[\W]*[A-Za-z]+[\W]*[\w]*", password):
            return True
