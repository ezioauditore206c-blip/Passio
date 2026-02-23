import string
import random
import math
import argparse
__version__ = "2.0.4"
class Passio:
    def __init__(self):
        pass



    def generate_password(self, length=12) -> str:
        chars = string.ascii_letters + string.digits + string.punctuation
        return ''.join(random.choice(chars) for _ in range(length))


    def calculate_entropy(self, password: str) -> float:
        pool = 0

        if any(c.islower() for c in password):
            pool += 26
        if any(c.isupper() for c in password):
            pool += 26
        if any(c.isdigit() for c in password):
            pool += 10
        if any(c in string.punctuation for c in password):
            pool += len(string.punctuation)
        if pool == 0:
            return 0.0
        return round(len(password) * math.log2(pool), 2)



    def strength_level(self, password: str) -> str:
        entropy = self.calculate_entropy(password)
        if entropy < 28:
            return "Very Weak"
        elif entropy <36:
            return "Weak"
        elif entropy < 60:
            return "Medium"
        elif entropy < 80:
            return "Strong"
        else:
            return "Very Strong"


    def feedback(self, password:str) -> dict:
        entropy = self.calculate_entropy(password)
        level = self.strength_level(password)
        return {
            "password":password,
            "length":len(password),
            "entropy":entropy,
            "strength":level,
        }

    def feedback_tips(self, password:str) -> str:
        tips = []
        if len(password) < 8:
            tips.append("At least 8 characters needed")
        if not any(c.isupper() for c in password):
            tips.append("At least one uppercase letter needed")
        if not any(c.islower() for c in password):
            tips.append("At least one lowercase letter needed")
        if not any(c.isdigit() for c in password):
            tips.append("At least one number letter needed")
        if not any(c in string.punctuation for c in password):
            tips.append("At least one special character needed")
        if not tips:
            return "your password looks strong"
        return " | ".join(tips)


