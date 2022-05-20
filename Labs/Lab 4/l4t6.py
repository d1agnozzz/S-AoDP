
from queues import stack

nums = stack()
letters = stack()
others = stack()

with open('character_mess.txt', 'r') as f:
    text = ''.join(f)

    for char in text:
        if char.isdigit():
            nums.pushright(char)
            continue
        elif char.isalpha():
            letters.pushright(char)
            continue
        else:
            others.pushright(char)
            continue

    reverse = stack()
    while not nums.is_empty():
        reverse.pushright(nums.popright())
    while not reverse.is_empty():
        print(reverse.popright())

    while not letters.is_empty():
        reverse.pushright(letters.popright())
    while not reverse.is_empty():
        print(reverse.popright())

    while not others.is_empty():
        reverse.pushright(others.popright())
    while not reverse.is_empty():
        print(reverse.popright())

        




# Old code with just one stack and temp list

# s = stack()

# with open('character_mess.txt', 'r') as f:
#     text = ''.join(f)

#     for char in text:
#         if s.is_empty():
#             s.pushright(char)
#             continue

#         if char.isdigit():
#             if s.peekright().isdigit():
#                 s.pushright()
#             else:
#                 temp = []
#                 while not s.is_empty() and not s.peekright().isdigit():
#                     temp.insert(0, s.popright())

#                 s.pushright(char)

#                 for element in temp:
#                     s.pushright(element)
        
#         elif char.isalpha():
#             if s.peekright().isalpha():
#                 s.pushright(char)
#             else:
#                 temp = []
#                 while not s.is_empty() and not s.peekright().isalpha():
#                     temp.insert(0, s.popright())
#                 s.pushright(char)
#                 for element in temp:
#                     s.pushright(element)

#         else:

#             s.pushright(char)

#     print(''.join(s.content))