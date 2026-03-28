# Class containing Pascal's Triangle row generation logic
class Solution:
    # Function to generate the Nth row of Pascal's Triangle
    def getNthRow(self, N):
        # Result list to store the row
        row = []
        
        # First value of the row is always 1
        val = 1
        row.append(val)
        
        # Compute remaining values using the relation:
        # C(n, k) = C(n, k-1) * (n-k) / k
        for k in range(1, N):
            val = val * (N - k) // k
            row.append(val)
        
        return row

# Example usage
N = 5  # Example: 5th row
sol = Solution()
result = sol.getNthRow(N)

# Print the row
print(*result)
