# class Solution:
#      # Function to set entire row and column to 0 if an element in the matrix is 0
#     def setZeroes(self, matrix):
#         # Get number of rows
#         m = len(matrix)
#         # Get number of columns
#         n = len(matrix[0])

#         # First pass: mark rows and columns
#         for i in range(m):
#             for j in range(n):
#                 # If current cell is zero
#                 if matrix[i][j] == 0:
#                     # Mark entire row
#                     for col in range(n):
#                         if matrix[i][col] != 0:
#                             matrix[i][col] = -1
#                     # Mark entire column
#                     for row in range(m):
#                         if matrix[row][j] != 0:
#                             matrix[row][j] = -1

#         # Second pass: replace -1 with 0
#         for i in range(m):
#             for j in range(n):
#                 if matrix[i][j] == -1:
#                     matrix[i][j] = 0

# # Driver code
# matrix = [[1,1,1],[1,0,1],[1,1,1]]
# sol = Solution()
# sol.setZeroes(matrix)
# for row in matrix:
#     print(row)

class Solution:
    # Function to set entire row and column to 0 if an element in the matrix is 0
    def setZeroes(self, matrix):
        # Get number of rows
        m = len(matrix)
        # Get number of columns
        n = len(matrix[0])

        # Create row marker array
        row = [0] * m
        # Create column marker array
        col = [0] * n

        # First pass: mark rows and columns that need to be zeroed
        for i in range(m):
            for j in range(n):
                # If element is zero, mark its row and column
                if matrix[i][j] == 0:
                    row[i] = 1
                    col[j] = 1

        # Second pass: set cells to zero based on markers
        for i in range(m):
            for j in range(n):
                # If the row or column is marked, set cell to zero
                if row[i] == 1 or col[j] == 1:
                    matrix[i][j] = 0

# Driver code
matrix = [[1,1,1],[1,0,1],[1,1,1]]
obj = Solution()
obj.setZeroes(matrix)
for r in matrix:
    print(r)
