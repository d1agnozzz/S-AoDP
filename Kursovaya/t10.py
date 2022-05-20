

def phoenix(n, k, string):
    sstr = ''.join(sorted(string))

    if k == 1:
        return ''.join(sstr)

    # if min(sstr) occurencies less than k or k = n 
    if sstr[0] != sstr[k-1] or n == k :
        return sstr[k-1]

    ans = sstr[0]

    # if remaining are NOT the same
    if sstr[k] != sstr[n-1]:   
        ans += sstr[k:n]

    else:
        # if same, distribute evenly
        for _ in range((n-1)//k):
            ans += sstr[n-1]

    return ans

print(phoenix(4, 2, 'baba'))
print(phoenix(5, 2, 'baacb'))
print(phoenix(5, 3, 'baacb'))
print(phoenix(5, 3, 'aaaaa'))
print(phoenix(6, 4, 'aaxxzz'))
print(phoenix(7, 1, 'phoenix'))


data_size = int(input())
for _ in range(data_size):
    n, k = list(map(int, input().split()))
    s = input()
    print(phoenix(n, k, s))