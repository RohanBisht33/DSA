class Solution:
    def binarySearch(self, array,k):
        left = 0
        right = len(array)-1
        ans = right+1
        while(left<=right):
            mid = (left+(right-left))//2
            if(array[mid]>=k):
                ans = mid
                right = mid -1
            else:
                left = mid+1
        return ans

nums = []
k = int(input())
t = int(input())
while t:
    nums.append(int(input()))
    t -= 1

sol = Solution()
print(sol.binarySearch(nums,k))