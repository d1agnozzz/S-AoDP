def reverso_lexycograph(n, costs, strs):
    r_strs = [strs[i][::-1] for i in range(n)]  # reversed

    from math import inf
    maxx = inf

    dp = [[maxx, maxx] for i in range(n)]
    # not reversed
    dp[0][0] = 0
    # reversed (cost wasted)
    dp[0][1] = costs[0]

    for i in range(1, n):

        if r_strs[i] >= strs[i - 1]:
            dp[i][1] = dp[i - 1][0] + costs[i]
        if r_strs[i] >= r_strs[i - 1]:
            dp[i][1] = min(dp[i][1], dp[i - 1][1] + costs[i])
        if strs[i] >= r_strs[i - 1]:
            dp[i][0] = dp[i - 1][1]
        if strs[i] >= strs[i - 1]:
            dp[i][0] = min(dp[i][0], dp[i - 1][0])
    ans = min(dp[-1])
    if ans >= maxx:
        return -1
    else:
        return ans

print(reverso_lexycograph(2, [1, 2], ['ba', 'ac']))
print(reverso_lexycograph(3, [1, 3, 1], ['aa', 'ba', 'ac']))
print(reverso_lexycograph(2, [5, 5], ['bbb', 'aaa']))
print(reverso_lexycograph(2, [3, 3], ['aaa', 'aa']))


n = int(input())
costs = list(map(int, input().split()))

strs = [input() for i in range(n)]
print(reverso_lexycograph(n, costs, strs))