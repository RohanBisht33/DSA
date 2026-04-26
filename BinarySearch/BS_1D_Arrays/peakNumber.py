class Solution:
    def peakNo(self, array):
        low,high = 0, len(array)-1

        while(low<high):
            mid = (high-low)//2

            if array[mid]>array[mid-1]:
                low = mid
            else:
                high = mid-1
        return array[low]

nums = []
t = int(input())
while t:
    nums.append(int(input()))
    t -= 1

sol = Solution()
print(sol.peakNo(nums))