# Class to solve 3-sum problem
class Solution:
    # Function to find triplets with sum zero
    def threeSum(self, arr, n):
        # Store unique triplets
        st = set()

        # First loop for first element
        for i in range(n):
            # Second loop for second element
            for j in range(i + 1, n):
                # Third loop for third element
                for k in range(j + 1, n):
                    # If triplet sum is zero
                    if arr[i] + arr[j] + arr[k] == 0:
                        # Store sorted triplet to avoid duplicates
                        triplet = tuple(sorted([arr[i], arr[j], arr[k]]))
                        st.add(triplet)

        # Convert set to list of lists
        return [list(triplet) for triplet in st]

# Driver code
if __name__ == "__main__":
    arr = [-1, 0, 1, 2, -1, -4]
    n = len(arr)
    obj = Solution()
    res = obj.threeSum(arr, n)
    for triplet in res:
        print(triplet)
