class Solution:
    def leaders(self, array):
        
        num = []
        i = 0
        n = len(array)
        isLeader = False
        max = n-1

        for i in range(n-1,-1,-1):
            if(array[i] >= array[max]):
                num.append(array[i])
                max = i
            

        # for i in range(n):
        #     if(i == n-1):
        #         num.append(array[i])
        #         break
        #     for j in range(i+1, n):
        #         if(array[j] > array[i]):
        #             isLeader = False
        #             break
        #         else:
        #             isLeader = True
        #     if(isLeader):
        #         num.append(array[i])

        
        num = num[::-1]
        return num

nums = []
t = int(input())
while t:
    nums.append(int(input()))
    t -= 1

sol = Solution()
print(sol.leaders(nums))