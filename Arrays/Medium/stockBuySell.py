class Solution:
    def stockBuySell(self, arr, n):
        print("hi")
        diff = 0
        maxProfit = 0
        print("running")
        for i in range(n):
            print("i = ", i)
            for j in range(i, n):
                print("j = ", j)
                diff = arr[j] - arr[i]
                print("difference = ", diff)

                if(diff <= 0):
                    diff = 0
                
                elif(diff > maxProfit):
                    maxProfit = diff
                    print("profit = ", maxProfit)
        
        return maxProfit


sol = Solution()
t = int(input())
n = t
nums = []
while t:
    nums.append(int(input()))
    t-=1

print("hello")
print(sol.stockBuySell(nums, n))