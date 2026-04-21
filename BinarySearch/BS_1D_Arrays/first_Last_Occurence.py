class Solution:
    def searchRange(self, arr, target):
        ls = []
        low,high = 0, len(arr)-1
        while low<=high:
            mid = low + (high-low)//2
            if(arr[mid]==target):
                ls.append(mid)
                low = mid+1
            elif(arr[mid]<target):
                high = mid-1
            else:
                low = mid+1
        return ls

nums = []
target= int(input())
t = int(input())
while t:
    nums.append(int(input()))
    t -= 1

sol = Solution()
print(sol.searchRange(nums, target))