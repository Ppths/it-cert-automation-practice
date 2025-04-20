#!/usr/bin/env python3

import re

def validate_user(username, minlen):

    # Lista de caracteres prohibidos al inicio

    forbidden_start = ['.', '_']



    # Verifica si el nombre es suficientemente largo

    if len(username) < minlen:

        return False



    # Verifica si el primer carácter es prohibido

    if username[0] in forbidden_start:

        return False



    # Verifica si el nombre es alfanumérico o contiene solo '_' y '.'

    for char in username:

        if not (char.isalnum() or char in "_."):

            return False



    return True


print(validate_user("blue.kale", 3)) # True

print(validate_user(".blue.kale", 3)) # Currently True, should be False

print(validate_user("red_quinoa", 4)) # True

print(validate_user("_red_quinoa", 4)) # Currently True, should be False

