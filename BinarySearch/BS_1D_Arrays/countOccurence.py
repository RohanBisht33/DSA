class Solution:
    def countOccurence(self, array,k):
        left = 0
        right = len(array)-1
        count = -1
        while(left<=right):
            mid = left+(right-left)//2
            if(array[mid]==k):
                count +=1
                left = mid + 1
                
            elif(array[mid]>k):
                right = mid - 1
            else:
                left = mid + 1
        return count+1

nums = []
k = int(input())
t = int(input())
while t:
    nums.append(int(input()))
    t -= 1

sol = Solution()
print(sol.countOccurence(nums,k))