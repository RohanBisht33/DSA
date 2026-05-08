from typing import List

class PainterPartition:
    # Count painters required for a given max allowed time
    def count_painters(self, boards: List[int], time: int) -> int:
        painters = 1
        boards_painter = 0

        for board in boards:
            if boards_painter + board <= time:
                boards_painter += board
            else:
                painters += 1
                boards_painter = board

        return painters

    # Use binary search to find the minimum time
    def find_largest_min_distance(self, boards: List[int], k: int) -> int:
        low = max(boards)
        high = sum(boards)
        result = high

        while low <= high:
            mid = (low + high) // 2
            painters = self.count_painters(boards, mid)

            if painters > k:
                low = mid + 1  # Too few painters, increase time
            else:
                result = mid   # Valid time, try reducing it
                high = mid - 1

        return result

# Test
boards = [10, 20, 30, 40]
k = 2
pp = PainterPartition()
ans = pp.find_largest_min_distance(boards, k)
print("The answer is:", ans)  # Expected: 60
