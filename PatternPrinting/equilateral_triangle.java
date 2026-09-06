import java.util.Scanner;

class Solution {
    public void pattern(int n) {
    
        for(int j = 1; j < n+1; j++){
            for(int i = n/2; i>=0; i--){
                System.out.print(" ");
                for(int k = 0; k < j*2 + 1; j++){
                    System.out.print("*");
                }
                System.out.println("");
            }
            
        }
        
    }
}

public class equilateral_triangle {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        Solution sol = new Solution();

        System.out.println("Enter n: ");
        int n = input.nextInt();

        sol.pattern(n);
    }
}