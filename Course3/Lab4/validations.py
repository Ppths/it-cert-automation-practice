def validate_user(username, minlen):

    forbidden_start = ['.', '_']



    if len(username) < minlen:

        return False



    if username[0] in forbidden_start:

        return False

    for char in username:

        if not (char.isalnum() or char in "_."):

            return False



    return True


print(validate_user("blue.kale", 3)) # True

print(validate_user(".blue.kale", 3)) # Currently True, should be False

print(validate_user("red_quinoa", 4)) # True

print(validate_user("_red_quinoa", 4)) # Currently True, should be False

