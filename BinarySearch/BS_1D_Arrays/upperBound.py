class Solution:
    def upperBound(self, array, k):
        low,high = 0, len(array)-1
        ans = len(array)
        while(low<=high):
            mid = (low+high)//2
            if(array[mid]<=k):
                low = mid +1
            else:
                ans = mid
                high = mid -1

        return ans

nums = []
k = int(input())
t = int(input())
while t:
    nums.append(int(input()))
    t -= 1

sol = Solution()
print(sol.upperBound(nums,k))