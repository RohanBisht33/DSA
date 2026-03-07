class Solution:
    def nextPermutation(self, nums):
        n = len(nums)

        # Step 1: find breakpoint
        i = n - 2 #second last element
        while i >= 0 and nums[i] >= nums[i+1]: #while descending order, move to the range position
            i -= 1

        # Step 2: find next greater element
        if i >= 0: 
            j = n - 1
            print(i,j)
            while nums[j] <= nums[i]:
                j -= 1
            nums[i], nums[j] = nums[j], nums[i]

        # Step 3: reverse suffix
        nums[i+1:] = reversed(nums[i+1:])
        
        return nums

nums = []
t = int(input())
while t:
    nums.append(int(input()))
    t -= 1

sol = Solution()
print(sol.nextPermutation(nums))