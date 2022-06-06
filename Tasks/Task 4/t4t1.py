def longest_unique(s):
    maxs = str()
    cur = str()
    for char in s:
        if char in cur:
            cur = str()

        cur += char

        if len(cur) > len(maxs):
            maxs = cur

    return maxs, len(maxs)

print(longest_unique('abcabcd'))
print(longest_unique('bbbb'))
print(longest_unique('pwwkew'))