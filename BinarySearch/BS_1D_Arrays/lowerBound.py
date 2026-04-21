class Solution:
    def lowerBound(self, array,k):
        left = 0
        right = len(array)-1
        ans = len(array)
        while(left<=right):
            mid = left+(right-left)//2
            if(array[mid]>=k):
                ans = mid
                right = right -1
            else:
                left = left +1
        return ans

nums = []
k = int(input())
t = int(input())
while t:
    nums.append(int(input()))
    t -= 1

sol = Solution()
print(sol.lowerBound(nums,k)) 

#It gives first and smallest index where element is found or can be placed