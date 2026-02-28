class Solution:
    def majorityElement(self, nums):
        n = len(nums)
        hash = {}

        for i in nums:
            hash[i] = hash.get(i, 0) + 1
        
        return (max(hash, key=hash.get))


sol = Solution()
print(sol.majorityElement([-1, -1, -1, -1]))
print(sol.majorityElement([2, 1, 3, 1, 2]))