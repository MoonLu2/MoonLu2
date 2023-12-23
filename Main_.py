import random

print('Введите длинну генерируемого пароля')
len_max = int(input('>'))
passsimbols = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
password = ''
for i in range(len_max):
    password += random.choice(passsimbols)

print('Пароль сгенерирован:')
print(password)
