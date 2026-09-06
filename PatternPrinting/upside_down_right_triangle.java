import java.util.Scanner;

class Solution {
    public void pattern(int n) {
        for(int i = n; i>0; i--){
            for(int j = 0; j <i; j++){
                System.out.print("*");
            }
            System.out.println("");
        }
        
    }
}

public class upside_down_right_triangle {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        Solution sol = new Solution();

        System.out.println("Enter n: ");
        int n = input.nextInt();

        sol.pattern(n);
    }
}