class Solution:
    def sortIt(self,nums):
        low = 0
        mid = 0
        size = len(nums)
        high = size-1
        for i in range(size):
            if(nums[mid] == 0):
                nums[mid], nums[low] = nums[low], nums[mid]
                low +=1
                mid +=1
            elif(nums[mid] == 1):
                mid +=1
            else:
                nums[mid], nums[high] = nums[high], nums[mid]
                high -=1
        
        return nums

sol = Solution()
t = int(input())
nums = []
while(t):
    nums.append(int(input()))
    t-=1

print(sol.sortIt(nums))