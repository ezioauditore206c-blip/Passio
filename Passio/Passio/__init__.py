import random
import string
from strength import calculate_entropy, strength_level

__version__ = "2.0.2"

class Passio:

    def __init__(self) -> None:
        pass


    def generate_password(self, length : int = 12) -> str:
        characters = string.ascii_letters + string.digits + string.punctuation
        return ''.join(random.choice(characters) for _ in range(length))

    def password_strength(self, password: str) -> str:
        entropy = calculate_entropy(password)
        level = strength_level(entropy)
        return {
            "password": password,
            "entropy" : entropy,
            "strength" : level,
            "length" : len(password)
        }
            
    def feedback_tips(self, password : str) -> str:
        tips = []

        if len(password) <8:
            tips.append("At least 8 characters needed.")
        if not any(c.isupper() for c in password):
            tips.append("At least one uppercase letter needed")
        if not any(c.islower() for c in password):
            tips.append("At least  one lowercase letter needed")
        if not any(c.isdigit() for c in password):
            tips.append("At least one number needed")
        if not any(c in string.punctuation for c in password):
            tips.append("At least one special character needed")
        if not tips:
            return "your password looks strong!"

        return "|".join(tips)
