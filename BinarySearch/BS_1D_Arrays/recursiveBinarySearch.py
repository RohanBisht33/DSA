class Solution:
    def recursiveBinarySearch(self, array, left, mid, right , element):

        mid = (left + (right-left))//2

        if(array[mid] == element):
            return mid
        if(array[mid] < element):
            return self.recursiveBinarySearch(array, left+1, mid, right, element)
        else:
            return self.recursiveBinarySearch(array, left, mid, right-1, element)
nums = []
element = int(input())
t = int(input())
while t:
    nums.append(int(input()))
    t -= 1

left = 0
right = len(nums)-1
mid = (left + (right-left))//2

sol = Solution()
print(sol.recursiveBinarySearch(nums,left,mid,right, element))