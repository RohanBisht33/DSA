class Solution:
    def nextPermutation(self, nums):
        n = len(nums)

        # Step 1: find breakpoint when it is last of that range
        i = n - 2 #start from second last element
        while i >= 0 and nums[i] >= nums[i+1]: #while descending order, move to the range position, it works for variable length
            i -= 1 #reach range

        # Step 2: find next greater element
        if i >= 0: #as long as it is still alive
            j = n - 1 #put j as last number

            while nums[j] <= nums[i]: #while j is less than i
                j -= 1  #reduce j so that j is greater than i
            nums[i], nums[j] = nums[j], nums[i] #then swap the range with next bigger number

        # Step 3: reverse suffix
        nums[i+1:] = reversed(nums[i+1:]) # in the end reverse the array except range(fully for last number)
        
        return nums

nums = []
t = int(input())
while t:
    nums.append(int(input()))
    t -= 1

sol = Solution()
print(sol.nextPermutation(nums))