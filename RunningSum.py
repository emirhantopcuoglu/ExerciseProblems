# Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).

# Return the running sum of nums.

class Solution:
    def runningSum(self, nums: list[int]) -> list[int]:
        nums2 = []
        sum = 0 
        for i in nums:
            sum = sum + i
            nums2.append(sum)
        return nums2

x = Solution()
nums = [1,2,3,4]
print(x.runningSum(nums))