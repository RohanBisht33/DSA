class Solution:
    def twoSum(self, nums, target):
        size = len(nums)
        left = 0
        right = size-1
        sum = 0
        while(left < right):
            sum = nums[left] + nums[right]
            if(sum > target):
                right -= 1
            elif(sum < target):
                left += 1
            else:
                return [left,right]
            
sol = Solution()
print(sol.twoSum([1, 3, 5, 7, 9], 8))