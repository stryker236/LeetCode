class Solution:
    def rob(self, nums):
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums)

        for i in range(2, len(nums)):
            nums[i] = max(nums[i - 2] + nums[i], nums[i - 1])
            print(f"i: {i}, nums: {nums}")

        return nums[-1]
    


# Example usage:
print(Solution().rob([2, 7, 9, 3, 1]))  # Output: 12
