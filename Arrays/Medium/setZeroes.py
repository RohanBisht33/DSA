class Solution:
    def setZeroes(self, matrix):

        rows = len(matrix)
        cols = len(matrix[0])

        zeros = []

        # Step 1: find all zero positions
        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == 0:
                    zeros.append((i, j))

        # Step 2: mark rows and columns
        for r, c in zeros:

            # make row zero
            for j in range(cols):
                matrix[r][j] = 0

            # make column zero
            for i in range(rows):
                matrix[i][c] = 0

        return matrix







nums = []

rows = int(input())
cols = int(input())

for _ in range(rows):
    row = list(map(int, input().split()))
    nums.append(row)

sol = Solution()
print(sol.setZeroes(nums))