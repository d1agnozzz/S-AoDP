def check_solvability((tags: list[int]) -> bool:
    check_sum = 0
    for ind1, pivot in enumerate(tags):
        for ind2, element in enumerate(tags[ind1:]):
            if element < pivot and element != 0:
                check_sum += 1
    check_sum += tags.index(0) // 4 + 1
    print("check sum: " + check_sum)

    return check_sum % 2 == 0


tags = [12, 5, 8, 7, 4, 11, 2, 13, 6, 1, 0, 10, 9, 15, 14, 3]

unsolvable_tags = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 15, 14, 0]

print(check_solvability(unsolvable_tags))
