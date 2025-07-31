import re


# Test Passed
def national_code_regex(code):
    """
    Check Validation Of National Codes
    :param code: National Code
    :return: Is Valid Or Not
    """
    if re.fullmatch("^\d{3}[-|\s]?\d{6}[-|\s]?\d", code):
        return True
    else:
        return False


# Test Passed
def phone_number_regex(number):
    """
    Check Validation Of Phone Numbers
    :param number: Phone Number
    :return:  Is Valid Or Not
    """
    if re.fullmatch("(0|\+98)?[-|\s]?9\d{2}[-|\s]?\d{3}[-|\s]?\d{4}", number):
        return True
    else:
        return False


# Test Passed
def email_address_regex(email):
    """
    Check Validation Of Email Address
    :param email: Email ID
    :return: Is Valid Or Not
    """
    if re.fullmatch("[a-zA-Z0-9][\w!#$%&'*+-/=?^_`{|}~.]{,63}@[a-z]{3,8}\.com", email):
        return True
    else:
        return False


# Test Passed
def name_regex(name):
    """
    Check Validation Of Names
    :param name: Name
    :return: Is Valid Or Not
    """
    if re.fullmatch("[a-zA-Z]{3,15}[\s\-]?[a-zA-Z]{0,15}[\s\-_]*[a-zA-Z]{,20}[\s\-]?[a-zA-Z]{0,10}", name):
        return True
    else:
        return False


# Test Passed
def address_regex(address):
    """
    Check Validation Of Address    :param address:
    :return: Is Valid Or Not
    """
    if re.fullmatch("[a-zA-Z\s\-_]{2,}(pelak)?[1-9]?\d{0,2}\s*", address, re.I):
        return True
    else:
        return False

if __name__ == '__main__':
    while True:
        arg = input("Enter: ")
        if address_regex(arg):
            print("Valid")
        else:
            print("Not Valid")
