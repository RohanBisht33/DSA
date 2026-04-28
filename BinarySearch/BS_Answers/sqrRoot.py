# class Solution:
#     # This function returns the floor value of the square root of a number
#     def mySqrt(self, x: int) -> int:
#         # Handle small numbers directly
#         if x < 2:
#             return x

#         # Initialize binary search range
#         left, right, ans = 1, x // 2, 0

#         # Perform binary search
#         while left <= right:
#             # Find middle point
#             mid = (left + right) // 2

#             # Check if mid*mid is less than or equal to x
#             if mid * mid <= x:
#                 # Store mid as potential answer
#                 ans = mid
#                 # Move to right half
#                 left = mid + 1
#             else:
#                 # Move to left half
#                 right = mid - 1

#         # Return final answer
#         return ans

# if __name__ == "__main__":
#     s = Solution()
#     print(s.mySqrt(8))

class Solution:
    def binarySearch(self, n):
        left = 0
        right = n-1
        while(left<=right):
            mid = left+(right-left)//2
            if(array[mid]==k):
                print(array)
                return mid
            elif(array[mid]>k):
                right = mid - 1
            else:
                left = mid + 1
        return -1

nums = []
t = int(input())

sol = Solution()
print(sol.binarySearch(nums,t))