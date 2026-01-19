class Solution:
    def rob(self, nums):
        def validCombinations(nums):
            
            sumMemo = {}
            combinations = []
            if len(nums) == 0:
                return [[]]
            if len(nums) == 1:
                return [nums]
            for i in range(2):
                current = nums[i]
                valids = validCombinations(nums[i + 2 :], )
                for valid in valids:
                    print("combinations so far:", combinations, "current:", current, "valid:", valid)
                    combinations.append([current] + valid)
            return combinations
        combinations = []
        combinations = validCombinations(nums)
        return max([sum(combination) for combination in combinations])




# Example usage:
print(Solution().rob([2, 7, 9, 3, 1]))  # Output: 12
