__version__ = "1.0.0"
class Passio():
    def __init__(self, password):
        self.password = password
    def check_strength(self):
        score = 0

        if len(self.password)>= 8:
            score += 1 
        if any(c.lower() for c in self.password):
            score += 1
        if any(c.isupper() for c in self.password):
            score += 1
        if any(c.isdigit() for c in self.password):
            score += 1
        if any(not c.isalnum() for c in self.password):
            score += 1

        if score <= 2:
            return "Poor"
        elif score <= 4:
            return "Medium"
        else:
            return "Strong"

