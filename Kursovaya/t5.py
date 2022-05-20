from math import inf

def monster_bullets(array):
    bullets = 0
    prev_exp = array[-1][-1]
    candidate = 0

    mini = inf

    for hp, exp in array:
        if hp > prev_exp:
            bullets += hp - prev_exp
            candidate = prev_exp
        else:
            candidate = hp

        if candidate < mini:
            mini = candidate

        prev_exp = exp
    return bullets + mini

games = int(input())
for _ in range(games):
    monsters = int(input())
    characteristics = list()
    for monster in range(monsters):
        characteristics.append(list(map(int, input().split(' '))))
    print(monster_bullets(characteristics)) 