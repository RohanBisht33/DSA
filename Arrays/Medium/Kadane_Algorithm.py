class Solution:
    def kadanes(self, nums):
        maximum = min(nums)
        print("size", len(nums), "max", maximum, "array", nums)
        end = 0
        sum = 0
        started = 0
        for i in range(len(nums)):
            if(sum == 0):
                start = i
            print("i = ", i)
            sum += nums[i]
            print("new sum = ", sum )

            if sum>maximum :
                maximum = sum
                started = start
                end = i
            elif sum < 0:
                sum = 0
            print("new max = ", maximum)
        return list([started, end])
    
sol = Solution()
t = int(input())
nums = []
while t:
    nums.append(int(input()))
    t-=1
print(sol.kadanes(nums))

# O(n^2)
# class Solution:
#     def kadanes(self, nums):
#         maximum = min(nums)
#         print("size", len(nums), "max", maximum, "array", nums)
#         for i in range(len(nums)):
#             print("i = ", i)
#             sum = 0
#             for j in range(i, len(nums)):
#                 print("j = ", j)
#                 sum += nums[j]
#                 print("new sum = ", sum)
#                 maximum = max(sum, maximum)
#                 print("new max = ", maximum)

#         return maximum
# sol = Solution()
# print(sol.kadanes([-2, -3, -7, -2, -10, -4]))


# O(n^3)
# class Solution:
#     def kadanes(self, nums):
#         maximum = min(nums)
#         print("size", len(nums), "max", maximum, "array", nums)
#         for i in range(len(nums)):
#             print("i = ", i)
#             for j in range(i, len(nums)):
#                 print("j = ", j)
#                 sum = 0
#                 for k in range(i, j+1):
#                     print("k = ", k)
#                     sum+= nums[k]
#                     print("new sum = ", sum)
#                 maximum = max(sum, maximum)
#                 print("new max = ", maximum)

#         return maximum
# sol = Solution()
# print(sol.kadanes([-2, -3, -7, -2, -10, -4]))
