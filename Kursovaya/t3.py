def is_possible_to_cook(needed, availale, prices, money, guess):
    bread = max(0, guess * needed[0] - availale[0]) * prices[0]
    sausage = max(0, guess * needed[1] - availale[1]) * prices[1]
    cheese = max(0, guess * needed[2] - availale[2]) * prices[2]

    return bread + sausage + cheese <= money


def max_burgers(recipe: str, available, prices, money):
    b_needed = recipe.count("B")
    s_needed = recipe.count("S")
    c_needed = recipe.count("C")

    needed = (b_needed, s_needed, c_needed)

    guess = sum(available) + money

    l = 0
    r = guess

    while r >= l:
        mid = (l + r) // 2

        if is_possible_to_cook(needed, available, prices, money, mid):
            l = mid + 1
        else:
            r = mid - 1
    return r


if __name__ == "__main__":
    recipe = input()
    available = list(map(int, input().split(" ")))
    prices = list(map(int, input().split(" ")))
    money = int(input())

    print(max_burgers(recipe, available, prices, money))
