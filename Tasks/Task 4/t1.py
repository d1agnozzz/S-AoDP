def longest_unique(string: str):
    maxs = str()
    maxlen = 0
    cur = str()
    curlen = 0
    uniques = set()
    for ind, char in enumerate(string):
        if char in uniques:
            cur = str()
            curlen = 0
            uniques = set()

        cur += char
        curlen += 1
        uniques.add(char)
        
        if curlen > maxlen:
                maxs = cur
                maxlen = curlen

    return maxs, maxlen

print(longest_unique('abcabcd'))
print(longest_unique('bbbb'))
print(longest_unique('pwwkew'))