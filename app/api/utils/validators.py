import re


class Validators():
    """docstring forValidators."""
    @classmethod
    def check_email(cls, email):
        if re.match(r"[\w\d]{3,}@[\w]+\.[\w]{2,4}", email):
            return True

    def check_username(cls,username):
        pass

    def check_location(cls, location):
        pass

    def check_password(cls, password):
        pass
