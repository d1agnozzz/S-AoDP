def min_right_ngon(N: int):
    if 3 <= N <= 5:
        return N
    
    for div in range(3, N//2+1):
        if N % div == 0:
            return div

print(min_right_ngon(87))
print(min_right_ngon(527))
print(min_right_ngon(866))
print(min_right_ngon(115))
print(min_right_ngon(8))
print(min_right_ngon(17))