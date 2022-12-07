import re

def validate_password_strenght(password: str) -> bool:
    '''Function takes string as an argument, delets possible
    spases at the begining and in the end, checks if the string
    contains required charcters and returns "bool" value'''

    p = password.strip()
    return bool(re.match(r'^(?=.*[0-9])'\
                        r'(?=(.*[a-z]){2,})'\
                        r'(?=(.*[A-Z]){2,})'\
                        r'(?=(.*[!@#$%^&*)(?.><;:\"]))'\
                        r'.{8,32}$', p))



