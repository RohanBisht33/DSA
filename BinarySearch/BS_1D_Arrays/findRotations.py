# class Solution:
#     def findKRotation(self, array):
#         low,high = 0, len(array)-1
#         min_e = min(array)
#         while(low<=high):
#             mid = low +(high-low)//2

#             if array[mid] == min_e:
#                 return mid
#             if array[mid] >= array[high]:
#                 if array[low] < min_e < array[mid]:
#                     high = mid-1
#                 else:
#                     low = mid +1   
#             else:
#                 if array[mid] > min_e > array[high]:
#                     low = mid +1
#                 else:
#                     high = mid-1

#         return -1

# nums = []
# t = int(input())
# while t:
#     nums.append(int(input()))
#     t -= 1

# sol = Solution()
# print(sol.findKRotation(nums))

class Solution:
    def findKRotation(self, array):
        low,high = 0, len(array)-1

        while(low<high):
            mid = low +(high-low)//2
            
            if array[high] < array[mid]:
                low = mid +1 
            else:
                high = mid 

        return low

nums = []
t = int(input())
while t:
    nums.append(int(input()))
    t -= 1

sol = Solution()
print(sol.findKRotation(nums))