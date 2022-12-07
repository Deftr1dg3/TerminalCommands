import re

def validate_password_strenght(password: str) -> bool:
    p = password.strip()
    return bool(re.match(r'^(?=.*[0-9])'\
                        r'(?=(.*[a-z]){2,})'\
                        r'(?=(.*[A-Z]){2,})'\
                        r'(?=(.*[!@#$%^&*)(?.><;:\"]))'\
                        r'.{8,32}$', p))




# made some changes
