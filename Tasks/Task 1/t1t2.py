def longest_palindrome(s: str):
    palindromes = set()
    max_len = 0
    for i in range(len(s)):
        for j in range(len(s)-1, i, -1):
            if s[i] == s[j] and i != j and j - i + 1 > max_len:
                front = i
                back = j
                while s[front] == s[back] and front < back:
                    front += 1
                    back -= 1
                if (front == back or front == back - 1) and s[front] == s[back]:
                    palindromes.add(s[i:j+1])
                    max_len = j - i + 1
    return max(palindromes, key = len)
s = 'eeee eeee eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee eeee'
print(longest_palindrome(s))
s = 'eeee ee eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee eeee'
print(longest_palindrome(s))