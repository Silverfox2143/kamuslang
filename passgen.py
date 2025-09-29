import random

def gen_pass(n):
    character = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
    password = ""

    for i in range(n):
       password += random.choice(character)

    return password



n = int(input("masukan panjang password: "))
print('hasil generate password:', gen_pass(n))