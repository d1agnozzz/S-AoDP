def hilberts_hotel(n, array):
    s = set()
    for k in range(n):
        new_room = (k + array[k])%n 
        if new_room in s:
            return "NO"
        s.add(new_room)
    return "YES"


print(hilberts_hotel(1, [14]))
print(hilberts_hotel(2, [-1, 1]))
print(hilberts_hotel(4, [5, 5, 5, 1]))
print(hilberts_hotel(3, [3, 2, 1]))
print(hilberts_hotel(2, [0, 1]))
print(hilberts_hotel(5, [-239, -2, -100, -3, -11]))
# print(hilberts_hotel(21, list(map(int, "-875686917 410529943 -707495183 127424171 247251083 130195224 -838443642 -833434989 -908630073 36578008 -158304369 -401354971 -932857686 34772737 -960777984 -817720620 -955394591 -918340921 276591458 -681756438 944119892".split(' ')))))

data_size = int(input())
for _ in range(data_size):
    n = int(input())
    a = list(map(int, input().split(' ')))
    print(hilberts_hotel(n, a))