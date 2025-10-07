class Solution:
    def merge(self,nums,low,mid,high):
        temp = []
        left = low
        right = mid+1
        while(left<=mid and right<=high):
            if(nums[left]<=nums[right]):
                temp.append(nums[left])
                left+=1
            else:
                temp.append(nums[right])
                right+=1
        while(left<=mid):
            temp.append(nums[left])
            left+=1
        while(right<=high):
            temp.append(nums[right])
            right+=1
        for i in range(len(temp)):
            nums[i+low] = temp[i]
    def merge_sort(self, nums, low, high):
        if(low>=high):
            return
        mid = (low+high)//2
        self.merge_sort(nums,low,mid)
        self.merge_sort(nums,mid+1,high)
        self.merge(nums,low,mid,high)
    def mergeSort(self, nums):
        low = 0
        high = len(nums)-1
        self.merge_sort(nums,low,high)
        return nums

if __name__ == "__main__":
    nums = [38, 27, 43, 3, 9, 82, 10]
    sol = Solution()
    sorted_nums = sol.mergeSort(nums)
    print("Sorted array:", sorted_nums)
