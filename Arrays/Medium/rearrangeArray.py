class Solution:
    def rearrange(self, array):
        i = 0
        j = 1
        arr = []
        for num in array:
            if(num>0):
                arr.insert(i, num)
                i+=2
            else:
                arr.insert(j, num)
                j+=2
        return arr

nums = []
t = int(input())
while(t):
    nums.append(int(input()))
    t-=1

sol = Solution()
print(sol.rearrange(nums))