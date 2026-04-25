class Solution:
    def binarySearch(self, array):
        left = 0
        right = len(array)-1
        while(left<=right):
            mid = left+(right-left)//2

            if array[mid] > array[right]:
                left = mid + 1
            else:
                right = mid -1
                

            # if(array[mid]>min_e and array[left+1]<min_e):
            #     print([array[x] for x in range(left,right+1)])
            #     right = mid - 1
            # else:
            #     print([array[x] for x in range(left,right+1)])
            #     left = mid + 1
            
        return array[left]

nums = []
t = int(input())
while t:
    nums.append(int(input()))
    t -= 1

sol = Solution()
print(sol.binarySearch(nums))