# class Solution:
#     # Function to search target in rotated sorted array using binary search
#     def search(self, nums, target):
#         # Set initial search space
#         low = 0
#         high = len(nums) - 1

#         # Run loop while valid search space exists
#         while low <= high:
#             # Find the middle index
#             mid = (low + high) // 2

#             # If target found at mid, return index
#             if nums[mid] == target:
#                 return mid

#             # Check if left half is sorted
#             if nums[low] <= nums[mid]:
#                 # If target lies in left half
#                 if nums[low] <= target < nums[mid]:
#                     high = mid - 1
#                 else:
#                     low = mid + 1
#             else:
#                 # Right half is sorted
#                 if nums[mid] < target <= nums[high]:
#                     low = mid + 1
#                 else:
#                     high = mid - 1

#         # Target not found
#         return -1

# # Driver code
# nums = [4,5,6,7,0,1,2]
# target = 0

# obj = Solution()
# result = obj.search(nums, target)

# print(result)

class Solution:
    def binarySearch(self, array,k):
        left = 0
        right = len(array)-1
        while(left<=right):
            mid = left+(right-left)//2
            if(array[mid]==k):
                #print(array)
                return mid
            if(array[left] ==k):
                return left
            if(array[right] ==k):
                return right
            elif(array[mid]>k and array[left]<k):
                #print([array[x] for x in range(left,right+1)])
                right = mid - 1
            else:
                #print([array[x] for x in range(left,right+1)])
                left = mid + 1
            
        return -1

nums = []
k = int(input())
t = int(input())
while t:
    nums.append(int(input()))
    t -= 1

sol = Solution()
print(sol.binarySearch(nums,k))