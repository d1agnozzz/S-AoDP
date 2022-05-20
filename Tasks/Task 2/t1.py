def validate_triangle(sides):
    for ind, side in enumerate(sides):
        second_side = sides[(ind+1)%3]
        third_side = sides[(ind+2)%3]
        if side >= second_side + third_side:
            return False
    return True

def longest_perimeter(lengths):
    sorted_lens = sorted(lengths)
    candidates = sorted_lens[-1:-4:-1]
    sorted_lens = sorted_lens[:-3]
    
    if validate_triangle(candidates):
        return sum(candidates)

    while  len(sorted_lens) != 0:
        if validate_triangle(candidates):
            return sum(candidates)
        maxi = candidates.index(max(candidates))
        candidates[maxi] = sorted_lens[-1]
    
    return 0
        

a = [2, 2, 3, 4]

longest_perimeter(a)
        

    