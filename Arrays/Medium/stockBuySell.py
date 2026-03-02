class Solution:
    def stockBuySell(self, arr, n):
        min_price = max(arr)
        maxProfit = 0

        for price in arr:
            if(price < min_price):
                min_price = price

            else:
                maxProfit = max(maxProfit, price-min_price)

        
        return maxProfit


# class Solution:
#     def stockBuySell(self, arr, n):
#         mini = arr[0]
#         maxi = arr[0]

#         for i in range(n):
#             print("i = ", i)

#             if(maxi < arr[i]):
#                 maxi = arr[i]

#             elif(mini >= arr[i]):
#                 mini = arr[i]

        
#         return maxi - mini

# class Solution:
#     def stockBuySell(self, arr, n):
#         print("hi")
#         diff = 0
#         maxProfit = 0
#         print("running")
#         for i in range(n):
#             print("i = ", i)
#             for j in range(i, n):
#                 print("j = ", j)
#                 diff = arr[j] - arr[i]
#                 print("difference = ", diff)

#                 if(diff <= 0):
#                     diff = 0
                
#                 elif(diff > maxProfit):
#                     maxProfit = diff
#                     print("profit = ", maxProfit)
        
#         return maxProfit


sol = Solution()
t = int(input())
n = t
nums = []
while t:
    nums.append(int(input()))
    t-=1

print(sol.stockBuySell(nums, n))