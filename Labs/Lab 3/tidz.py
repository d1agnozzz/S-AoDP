string = "щавлёвконстантинвладимирович"
quantity = {}

for char in string:
    if char not in quantity:
        quantity[char] = 1
    else: 
        quantity[char] = quantity.get(char) + 1

sort = {k: v for k, v in reversed(sorted(quantity.items(), key=lambda item: item[1]))}

for k, v in sort.items():
    print(f"{k}: {v}")

print(sum(sort.values()))