# Passio
**Version:** 2.0.4

Powerful password manager and analyzer with tips, strength check and generator.

---
## Features
-Generate secure passwords of any length
-Check password strength (entropy based)
-Interactive CLI for easy usage
-Python 3.8+ compatible

## Installaion
**From PyPI
```bash
pip install Passio
```
## Usage
```Python
from Passio import Passio
p = Passio()
password = "724242AA"
# Check strength
print(p.strength_level(password))
# Detailed feedback
print(p.feedback(password))
# Generate Strong Password
print(p.generate_password())
