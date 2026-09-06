import java.util.Scanner;

class Solution {
    public void pattern(int n) {
        
        for(int i = 1; i<=n; i++){
            for(int j = 0; j <i; j++){
                System.out.print(i);
            }
            System.out.println("");
        }
        
    }
}

public class right_angled_repeatition {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        Solution sol = new Solution();

        System.out.println("Enter n: ");
        int n = input.nextInt();

        sol.pattern(n);
    }
}