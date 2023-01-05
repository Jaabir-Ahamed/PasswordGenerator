import random
import string


def passwordgen():
    passwords = int(input("Please enter desired number for password length: "))
    if passwords < 0:
        print("Sorry password desired le is invalid...")
    password = ''
    for i in range(passwords):
        password += random.choice(string.ascii_uppercase)
    return password


print(passwordgen())
