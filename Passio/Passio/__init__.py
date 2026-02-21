import random
import string
from Passio import *

class Passio:
    def __init__(self):
        self.symbols = "!@#$%^&*()-_=+[]{}|;:,.<>?/~"
        

    def generate_password(self, length=12, use_symbols=True):
        chars = string.ascii_letters + string.digits
        if use_symbols:
            chars += self.symbols
        password = "".join(random.choice(chars) for _ in range(length))
        return password

    def password_strength(self, password):
        length = len(password)
        lower = any(c.islower() for c in password)
        upper = any(c.isupper() for c in password)
        digit = any(c.isdigit() for c in password)
        symbol = any(c in self.symbols for c in password)
        score = sum([lower, upper, digit, symbol])
        if length >= 12 and score == 4:
            return "Very Strong"
        elif length >= 8 and score >= 3:
            return "Strong"
        elif length >= 6 and score >= 2:
            return "Medium"
        else:
            return "Weak"


    def password_feedback(self, password):
        feedback = []
        if len(password) < 8:
            feedback.append("Password too short")
        if not any(c.isupper() for c in password ):
            feedback.append("Add uppercase letter")
        if not any(c.islower() for c in password):
            feedback.append("Add lowercase letter")
        if not any(c.isdigit() for c in password):
            feedback.append("Add digits")
        if not any(c in self.symbols for c in password):
            feedback.append("Add symbols")
