# class Solution:
#     def search_in_rotated_sorted_array_ii(self, arr, k):
#         low, high = 0, len(arr) - 1

#         while low <= high:
#             mid = (low + high) // 2

#             # If mid is the target
#             if arr[mid] == k:
#                 return True

#             # Cannot determine sorted half due to duplicates
#             if arr[low] == arr[mid] == arr[high]:
#                 low += 1
#                 high -= 1
#                 continue

#             # Left half is sorted
#             if arr[low] <= arr[mid]:
#                 if arr[low] <= k <= arr[mid]:
#                     high = mid - 1
#                 else:
#                     low = mid + 1
#             else:
#                 # Right half is sorted
#                 if arr[mid] <= k <= arr[high]:
#                     low = mid + 1
#                 else:
#                     high = mid - 1

#         return False


# if __name__ == "__main__":
#     arr = [7, 8, 1, 2, 3, 3, 3, 4, 5, 6]
#     k = 3
#     sol = Solution()
#     result = sol.search_in_rotated_sorted_array_ii(arr, k)

#     if result:
#         print("Target is present in the array.")
#     else:
#         print("Target is not present.")

class Solution:
    def binarySearch(self, array,k):
        left = 0
        right = len(array)-1
        while(left<=right):
            mid = left+(right-left)//2
            if(array[mid]==k):
                print(array)
                return True
            if(array[left] ==k):
                return True
            if(array[right] ==k):
                return True
            elif(array[mid]>k and array[left]<k):
                print([array[x] for x in range(left,right+1)])
                right = mid - 1
            else:
                print([array[x] for x in range(left,right+1)])
                left = mid + 1
            
        return False

nums = []
k = int(input())
t = int(input())
while t:
    nums.append(int(input()))
    t -= 1

sol = Solution()
print(sol.binarySearch(nums,k))