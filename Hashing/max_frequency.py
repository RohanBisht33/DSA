class Solution:
    def mostFrequentElement(self, nums):
        hash = {}

        for i in nums:
            hash[i] = hash.get(i,0) + 1

        max_value = max(hash.values())

        max_element = [k for k,v in hash.items() if(v == max_value)]

        return min(max_element)

if __name__ == "__main__":
    nums = [10,9,7]
    sol = Solution()
    print(sol.mostFrequentElement(nums))