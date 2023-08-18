num = 48 # 48, 12, 3
div = 4 # Devient 3 lorsque num devient 3 après être passé de 48, à 12 puis à 3

print(num, '=', ' ')
while (num > div) and (div>1):
    if num % div != 0:
        # num = 48 % 4 | 4, 8, 12... 40, 44, 48 v (On peut faire tenir 12 fois 4 dans 48)
        # num = 12 %
        # 48 % 5 | 5, 10, 15... 35, 40, 45, 50 x (On peut faire tenir 9 fois 5 dans 48 avec un reste de 3)
        div = div - 1
    num = num // div
    # 48 divisé par 4 = 12
    # 12 divisé par 4 = 3
    # 3 divisé par 4 est impossible par modulo
    print(div, 'x', end=' ')
print(num)
