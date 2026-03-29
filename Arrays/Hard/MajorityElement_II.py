from typing import List

class Solution:
    # Function to find majority elements in an array
    def majorityElementTwo(self, nums: List[int]) -> List[int]:
        
        # Size of the array
        n = len(nums)
        
        # List of answers
        result = []
        
        for i in range(n):
            """ Checking if nums[i] is not 
            already part of the answer """
            if len(result) == 0 or result[0] != nums[i]:
                
                cnt = 0
                
                for j in range(n):
                    # counting the frequency of nums[i]
                    if nums[j] == nums[i]:
                        cnt += 1
                
                # check if frequency is greater than n/3
                if cnt > (n // 3):
                    result.append(nums[i])
                
            # if result size is equal to 2 break out of loop
            if len(result) == 2:
                break
        
        # return the majority elements
        return result

if __name__ == "__main__":
    arr = [11, 33, 33, 11, 33, 11]
    
    # Create an instance of Solution class
    sol = Solution()
    
    ans = sol.majorityElementTwo(arr)
    
    # Print the majority elements found
    print("The majority elements are:", end=" ")
    for it in ans:
        print(it, end=" ")
    print()