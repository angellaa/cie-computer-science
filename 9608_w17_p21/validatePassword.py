#
# Variables:
#  - lowerCount : integer
#  - upperCount : integer
#  - numericCount : integer
#

def ValidatePassword(password):
    lowerCount = 0
    upperCount = 0
    numericCount = 0

    for c in password:
        if c.islower():
            lowerCount = lowerCount + 1
        elif c.isupper():
            upperCount = upperCount + 1
        elif c.isnumeric():
            numericCount = numericCount + 1

    return password.isalnum() and lowerCount >= 2 and upperCount >= 2 and numericCount >= 3


print(ValidatePassword("123ABab"))    # Expect: True
print(ValidatePassword("123 ABab"))   # Expect: False (non alphanumeric character)
print(ValidatePassword("123ABab;"))   # Expect: False (non alphanumeric character)
print(ValidatePassword("123ABa"))     # Expect: False (not enough lower case alphabetic characters)
print(ValidatePassword("123Aab"))     # Expect: False (non enough upper case alphabetic characters)
print(ValidatePassword("12ABab"))     # Expect: False (non enough numeric characters)
