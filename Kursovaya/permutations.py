def permutations(num: int):
    if num < 4:
        return '-1'
    if num == 4:
        return '3 1 4 2'
    else: 
        odd = list()
        for i in range(1, num+1, 2):
            odd.append(i)

        even = [4, 2]
        for i in range(6, num+1, 2):
            even.append(i)

        odd.reverse()

        return " ".join(map(str, odd+even))

quant = int(input())
inputs = list()
for i in range(quant):
    inputs.append(int(input()))
for i in inputs:
    print(permutations(i))
