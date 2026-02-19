class Solution:
    def majorityElement(self, nums):
        n = len(nums)
        hash = {}

        for i in nums:
            hash[i] = hash.get(i, 0) + 1
        
        return [k for k,v in hash.items() if v == (max(hash.values()))]


sol = Solution()
print(sol.majorityElement([-1, -1, -1, -1]))