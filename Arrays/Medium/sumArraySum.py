class Solution:
    # Function to find count of subarrays with sum equal to k
    def subarraySum(self, arr, k):
        # Size of the array
        n = len(arr)

        # Initialize count of subarrays
        count = 0

        # Traverse all possible start indices
        for i in range(n):
            # Traverse all possible end indices from start
            for j in range(i, n):
                # Initialize sum for current subarray
                total = 0

                # Calculate sum of subarray from i to j
                for m in range(i, j + 1):
                    total += arr[m]

                # If sum equals k, increment count
                if total == k:
                    count += 1

        # Return total count of subarrays
        return count


# Driver code
if __name__ == "__main__":
    # Input array
    arr = [3, 1, 2, 4]

    # Target sum
    k = 6

    # Create Solution object
    sol = Solution()

    # Call function and store result
    result = sol.subarraySum(arr, k)

    # Print the count of subarrays
    print("The number of subarrays is:", result)
