import re
from datetime import datetime

def payankhedmat_validator(payankhedmat):
    errors = []
    if not (type(payankhedmat[0]) == int and payankhedmat[0]>0):
        errors.append('Person ID must be an integer > 0')

    if not (type(payankhedmat[1]) == int and payankhedmat[1]>0):
        errors.append('Person Serial Number must be an integer > 0')

    if not (type(payankhedmat[2]) == str and re.match(r"^[a-zA-Z\s]{3,30}$", payankhedmat[2])):
        errors.append('Person Start Date must be an integer > 0')

    if not (type(payankhedmat[3]) == int and payankhedmat[3]>0):
        errors.append('Person End Date must be an integer > 0')

    if not (type(payankhedmat[4]) == str and re.match(r"^[a-zA-Z\s]{3,30}$", payankhedmat[4])):
        errors.append('Person City is invalid > 0')

    if not (type(payankhedmat[5]) == str and re.match(r"^[a-zA-Z\s]{3,30}$", payankhedmat[5])):
        errors.append('Person Organ is invalid')

    return errors