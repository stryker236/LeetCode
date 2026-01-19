def matrixSum(nums) -> int:
    score = 0
    candidates = []
    while nums[0]:
        for i, row in enumerate(nums):
            best = max(row)
            candidates.append(best)
            nums[i].remove(best)
        score += max(candidates)
        candidates = []
    return score

print(matrixSum([[7, 2, 1], [6, 4, 2], [6, 5, 3], [3, 2, 1]]))
