import re


class Validators():
    """docstring forValidators."""
    def check_email(email):
        if re.match(r"[\w\d]{3,}@[\w]+\.[\w]{2,4}", email):
            return True

    def check_username(username):
        if re.match(r"[^\W][A-Za-z]?[\w]?[-_]?[A-Za-z0-9]{3,}", username):
            return True

    def check_password(password):
        if re.match(r"[\W]*[A-Za-z]+[\W]*[\w]*", password):
            return True
