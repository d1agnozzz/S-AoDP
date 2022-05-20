def max_NOK(n):
    if n < 3:
        return n
    if n == 3:
        return 6
    else:
        if n % 2 != 0:
            return n * (n-1) * (n-2)
        elif n % 3 == 0:
            return (n-1) * (n-2) * (n-3)
        else: 
            return n * (n-1) * (n-3)

print(max_NOK(9))
print(max_NOK(7))

n = int(input())
print(max_NOK(n))
    