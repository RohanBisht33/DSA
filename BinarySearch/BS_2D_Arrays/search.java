import java.util.*;

class Solution {
    // Function to search target in a 2D matrix using binary search over a virtual 1D array
    public boolean searchMatrix(List<List<Integer>> matrix, int target) {
        // Get the number of rows
        int n = matrix.size();

        // Get the number of columns
        int m = matrix.get(0).size();

        // Set initial binary search range over the imaginary 1D array
        int low = 0, high = n * m - 1;

        // Perform binary search
        while (low <= high) {
            // Calculate the middle index of the virtual 1D array
            int mid = (low + high) / 2;

            // Convert mid index to corresponding 2D indices
            int row = mid / m;
            int col = mid % m;

            // Check if the target is found
            if (matrix.get(row).get(col) == target)
                return true;

            // If the target is greater, discard the left half
            else if (matrix.get(row).get(col) < target)
                low = mid + 1;

            // If the target is smaller, discard the right half
            else
                high = mid - 1;
        }

        // If not found, return false
        return false;
    }
}

// Driver code
public class search {
    public static void main(String[] args) {
        // Define a 2D matrix
        List<List<Integer>> matrix = new ArrayList<>();
        matrix.add(Arrays.asList(1, 2, 3, 4));
        matrix.add(Arrays.asList(5, 6, 7, 8));
        matrix.add(Arrays.asList(9, 10, 11, 12));

        // Create an object of the Solution class
        Solution obj = new Solution();

        // Call the function and print result
        if (obj.searchMatrix(matrix, 8))
            System.out.println("true");
        else
            System.out.println("false");
    }
}