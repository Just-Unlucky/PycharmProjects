from random import randrange
n = randrange(10000)
while True:
    v = int(input())
    if n == v:
        print('You win')
        break
    print('Smaller' if (n < v) ^ (randrange(4) < 1) else 'Bigger')