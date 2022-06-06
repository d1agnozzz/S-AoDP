def get_combinations(input_candidates: list(), target: int, input_combination: list() = list()):
    # input_candidates = sorted(input_candidates)
    ans = list()
    current_combination = input_combination.copy()
    for i in range(len(input_candidates)):
        temp_combination = current_combination + [input_candidates[i]]
        combination_sum = sum(temp_combination)
        if combination_sum > target:
            return ans
        if combination_sum == target:
            temp_combination = sorted(temp_combination)
            if not temp_combination in ans:
                ans.append(temp_combination)
                return ans
        if combination_sum < target:
            for combination in get_combinations(input_candidates, target, temp_combination):
                if not combination in ans:
                    ans.append(combination)
    
    return ans

print(get_combinations([2, 3, 5, 6, 7], 7))