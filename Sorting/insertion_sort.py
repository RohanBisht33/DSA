class Solution:
    def insertionSort(self, nums):
        for i in range(1, len(nums)):
            key = nums[i]
            j = i-1
            while(j >= 0 and nums[j] > key):
                nums[j+1] = nums[j]
                j -= 1
            nums[j+1] = key
        
        return nums

if __name__ == "__main__":
    nums = [64, 25, 12, 22, 11]
    print("Original array:", nums)
    Solution().insertionSort(nums)
    print("Sorted array:", nums)