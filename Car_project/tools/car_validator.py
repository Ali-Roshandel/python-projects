import re


def plate_validator(plate):
    return bool(re.fullmatch('\d{2}[A-Za-z]\d{3}', plate))


def text_validator(name):
    return bool(re.fullmatch('[A-Za-z\s]{2,30}', name))
