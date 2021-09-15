digits = '0123456789'
chars = 'abcdefghiklmn' \
    'opqrstuvwxyz'
up = chars.upper()
special = '_!$%&?'
all = digits+chars+special
from random import choice
password = ''.join(
    choice(all) for i in range(8)
)


print(password)