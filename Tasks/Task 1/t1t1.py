# Даны две строки: `s1` и `s2` с одинаковым размером.

# Проверьте, может ли некоторая перестановка строки `s1` “победить” некоторую перестановку строки `s2` или наоборот.

# Строка x может “победить” строку y (обе имеют размер n), если `x[i] >= y[i]` (в алфавитном порядке) для всех i от 0 до n-1.


def permatation_alphabetical(s1: str, s2: str):
    s1_in_order = sorted(s1)
    s2_in_order = sorted(s2)

    for i in range(len(s1)):
        if s1_in_order[i] > s2_in_order[i]:
            return False

    return True


s1 = "axy"
s2 = "cyz"

print(permatation_alphabetical(s1, s2))