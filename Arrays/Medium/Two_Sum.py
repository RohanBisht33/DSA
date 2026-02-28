class Solution:
    def twoSum(self, nums, target):
        size = len(nums)
        sum = nums[i]
        j = 0

        for i in range(size):
            sum += nums[j]
            if(sum > target):
                sum = 0
            elif(sum == target):
                return [n for n in range()]
            
sol = Solution()
print(sol.twoSum( [1, 3, 5, -7, 6, -3], 0))