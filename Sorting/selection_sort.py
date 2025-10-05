class Solution:
    def selectionSort(self, nums):
        for i in range(0, len(nums)-1):
            min = i
            for j in range(i+1,len(nums)):#back to work
                if(nums[j]<nums[min]):
                    min = j
            temp = nums[i]
            nums[i] = nums[min]
            nums[min] = temp
    
if __name__ == "__main__":
    nums = [64, 25, 12, 22, 11]
    print("Original array:", nums)
    Solution().selectionSort(nums)
    print("Sorted array:", nums)