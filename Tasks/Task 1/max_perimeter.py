
inputs0 = [3, 4, 5, 10, 15]
inputs1 = [1, 2, 1]
inputs2 = [3, 6, 2, 3, 8]
inputs3 = [3, 6, 2, 3, 3]



def maxPerimeter(side_lengths):
    temp = side_lengths.copy()
    temp = sorted(temp)
    candidates = [temp[i] for i in range(-3,0)]
    nextMinInd   = -4
    while (candidates[0] + candidates[1] <= candidates[2] or candidates[0] + candidates[2] <= candidates[1] or candidates[2] + candidates[1] <= candidates[0]) and abs(nextMinInd)<=len(temp):
        candidates[0] = temp[nextMinInd]
        nextMinInd -= 1
    print(candidates)
    if(candidates[0] + candidates[1] <= candidates[2] or candidates[0] + candidates[2] <= candidates[1] or candidates[2] + candidates[1] <= candidates[0]):
        return 0
    return sum(candidates)

print(maxPerimeter(inputs0))
print(maxPerimeter(inputs1))
print(maxPerimeter(inputs2))
print(maxPerimeter(inputs3))