# Passio
**Version:** 2.0.2

Powerful password manager and analyzer with tips, strength check, and interactive CLI.

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
from Passio import PAssio
p = Passio()
# Generate a password
password = p.generate_password(16)
print(password)

# Check strength
print(p.password_strength())

# Detailed feedback
print(p.feedback())
