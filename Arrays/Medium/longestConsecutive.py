class Solution:
    def longest(self, array):
        
        count = 1
        array.sort()
        max = 0
        for i in range(len(array)-1):
            if(array[i]+1 == array[i+1]):
                count +=1
                max = count
            else:
                count = 1
            
        return max

nums = []
t = int(input())
while t:
    nums.append(int(input()))
    t -= 1

sol = Solution()
print(sol.longest(nums))

