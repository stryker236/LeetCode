class Solution:
    def rob(self, nums):
        def bestSum(seq, memo):
            print("current sequence:", seq, "memo:", memo)
            if seq:
                if seq in memo:
                    return memo[seq]
                memo[seq] = max(seq[0] + bestSum(seq[2:], memo), bestSum(seq[1:], memo))
            else:
                memo[seq] = 0
            return memo[seq] 
        return bestSum(tuple(nums),{})

# Example usage:
print(Solution().rob([2, 7, 9, 3, 1]))  # Output: 12
