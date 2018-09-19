import hashlib
import itertools


def hash_with_sha256(str):
    hash_object = hashlib.sha256(str.encode('utf-8'))
    hex_dig = hash_object.hexdigest()
    return hex_dig


def check_passwords(check_pass):
    for key, value in hash_with_sha256.items():
        if value[2] == hash_with_sha256(value[1].join(check_pass)):
            print(key)


def password_in_list(salt, hashed, name, list_password):
    for password in list_password:
        hex_dig = hash_with_sha256(salt + password)
        if hashed == hex_dig:
            print(name + "has password" + password)

def main():
    x = input("Enter minimum password length ")  # The minimum input value which is 3
    y = input("Enter maximum password length")  # The maximum input value which is 7
    list_password = []

    for j in range(int(x), int(y) + 1):
        for i in itertools.product([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], repeat=int(j)):
            list_password.append(''.join(map(str, i)))
            print("password generated")

        break
    main()
