
from queues import stack

nums = stack()
letters = stack()
others = stack()

with open('character_mess.txt', 'r') as f:
    text = ''.join(f)

    for char in text:
        if char.isdigit():
            nums.push_right(char)
            continue
        elif char.isalpha():
            letters.push_right(char)
            continue
        else:
            others.push_right(char)
            continue

    reverse = stack()
    while not nums.is_empty():
        reverse.push_right(nums.pop_right())
    while not reverse.is_empty():
        print(reverse.pop_right())

    while not letters.is_empty():
        reverse.push_right(letters.pop_right())
    while not reverse.is_empty():
        print(reverse.pop_right())

    while not others.is_empty():
        reverse.push_right(others.pop_right())
    while not reverse.is_empty():
        print(reverse.pop_right())