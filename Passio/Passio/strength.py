import math
import string
def calculate_entropy(password:str) -> float :
    pool = 0

    if any(c.islower() for c in password):
        pool += 26
    if any(c.isupper() for c in password):
        pool += 26
    if any(c.isdigit() for c in password):
        pool += 10
    if any(c in string.punctuation for c in password):
        pool += len(string.punctuation)



    if pool ==0:
        return 0


    entropy = len(password) * math.log2(pool)
    return round(entropy, 2)



def strength_level(entropy: float) -> str:
    if entropy < 28:
        return "Very Weak"
    elif entropy <36:
        return "Weak"
    elif entropy < 60:
        return "Medium"
    elif entropy < 128:
        return "Strong"
    else:
        return "Very Strong"
