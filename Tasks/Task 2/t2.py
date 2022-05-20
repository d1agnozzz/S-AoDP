def greaterThan(a: int, b: int):
    first = str(a)
    second = str(b)

    min_len = min(len(first), len(second))

    for digit_ind in range(min_len):
        digit_a = int(first[digit_ind])
        digit_b = int(second[digit_ind])

        if digit_a > digit_b:
            return True
        elif digit_a == digit_b:
            if digit_ind == min_len - 1:
                if len(first) == len(second):
                    return False 

                if len(first) < len(second):
                    return greaterThan(int(first), int(second[min_len:]))
                else:
                    return greaterThan(int(first[min_len:]), int(second))
        else:
            return False

def insertion_sort(nums):
    for i in range(1, len(nums)):
        j = i - 1
        while j >= 0 and not greaterThan(nums[j], nums[j+1]):
            nums[j], nums[j+1] = nums[j+1], nums[j]
            j -= 1

def maximize(ints):
    result = str()
    insertion_sort(ints)

    for num in ints:
        result += str(num)
    
    result = result.lstrip('0')

    return result if result != '' else '0'

print(maximize([5, 3, 30, 34, 5, 9]))
print(maximize([0, 0]))
print(maximize([34323, 3432]))