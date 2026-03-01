class Solution:
    def kadanes(self, nums):
        maximum = min(nums)
        print("size", len(nums), "max", maximum, "array", nums)
        for i in range(len(nums)):
            print("i = ", i)
            sum = 0
            for j in range(i, len(nums)):
                print("j = ", j)
                sum += nums[j]
                print("new sum = ", sum)
                maximum = max(sum, maximum)
                print("new max = ", maximum)

        return maximum
sol = Solution()
print(sol.kadanes([-2, -3, -7, -2, -10, -4]))



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
