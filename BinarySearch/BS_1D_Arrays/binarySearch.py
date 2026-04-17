class Solution:
    def binarySearch(self, array,k):
        left = 0
        right = len(array)-1
        while(left<=right):
            mid = (left+(right-left))//2
            if(array[mid]==k):
                print(array)
                return mid
            elif(array[mid]>k):
                right = right - 1
            else:
                left = left + 1
        return -1

nums = []
k = int(input())
t = int(input())
while t:
    nums.append(int(input()))
    t -= 1

sol = Solution()
print(sol.binarySearch(nums,k))