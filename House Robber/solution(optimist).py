class Solution:
    def rob(self, nums):
        def robAmount(houses, depth=0, begin=None):
            if depth == 0:
                chosen = begin
            else:
                chosen = max(houses) # optimistic
            chosenIdx = houses.index(chosen)
            left = houses[:chosenIdx - 1] if chosenIdx - 1 >= 0 else [] 
            right = houses[chosenIdx + 2 :] if chosenIdx + 2 < len(houses) else []
            print(f"chosen house: {chosen} from {houses} at index {chosenIdx}, left: {left}, right: {right}")
            if left and right:
                return chosen + robAmount(left, depth + 1) + robAmount(right, depth + 1)
            elif left:
                return chosen + robAmount(left, depth + 1)
            elif right:
                return chosen + robAmount(right, depth + 1)
            return chosen
        options = []
        for i in range(len(nums)):
            options.append(robAmount(nums, begin=nums[i]))    
        print(f"options: {options}")
        return max(options)


# Example usage:
print(Solution().rob([2, 7, 9, 3, 1]))  # Output: 12
