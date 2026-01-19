class Solution:
    def matrixSum(self, nums) -> int:
        score = 0
        for row in nums:
            row.sort()  
        while nums[0]:
            candidates = []
            for i, row in enumerate(nums):
                candidates.append(row.pop())
            score += max(candidates)        
        return score
    

# Example usage:
print(Solution().matrixSum([[7,2,1],[6,4,2],[6,5,3],[3,2,1]]))  # Output: 15
