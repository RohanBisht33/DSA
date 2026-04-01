from collections import defaultdict
from typing import List

class Solution:
    # Function to find majority elements in an array
    def majorityElementTwo(self, nums: List[int]) -> List[int]:
        # Size of the array
        n = len(nums)

        # List of answers
        result = []

        # Declaring a map
        mpp = defaultdict(int)

        # Least occurrence of the majority element
        mini = n // 3 + 1

        # Storing the elements with its occurrence
        for num in nums:
            mpp[num] += 1

            # Checking if num is the majority element
            if mpp[num] == mini:
                result.append(num)

            # If result size is equal to 2 break out of loop
            if len(result) == 2:
                break

        # Return the majority elements
        return result

if __name__ == "__main__":
    arr = [11, 33, 33, 11, 33, 11]
    
    # Create an instance of Solution class
    sol = Solution()
    
    ans = sol.majorityElementTwo(arr)
    
    # Print the majority elements found
    print("The majority elements are:", *ans)