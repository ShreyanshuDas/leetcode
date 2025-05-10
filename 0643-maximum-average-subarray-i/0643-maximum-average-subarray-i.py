class Solution:
    def findMaxAverage(self, nums, k):
        current_sum = sum(nums[:k])
        max_sum = current_sum
        for i in range(k, len(nums)):
            current_sum += nums[i] - nums[i - k]
            if current_sum > max_sum:
                max_sum = current_sum
        return max_sum / float(k)

# Example usage:
param_1 = [1,12,-5,-6,50,3]
param_2 = 4
ret = Solution().findMaxAverage(param_1, param_2)
print(ret)  # Output: 12.75
