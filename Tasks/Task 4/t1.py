def longest_unique(s):
    max = str()
    cur = str()
    for char in s:
        if char in cur:
            cur = str()

        cur += char

        if len(cur) > len(max):
            max = cur

    return max, len(max)

print(longest_unique('abcabcd'))
print(longest_unique('bbbb'))
print(longest_unique('pwwkew'))