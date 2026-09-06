import java.util.Scanner;

class Solution {
    public void pattern(int n) {
        for(int i = 1; i<=n+1; i++){
            for(int j = 1; j <i; j++){
                System.out.print(j);
            }
            System.out.println("");
        }
        
    }
}

public class right_angled_series {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        Solution sol = new Solution();

        System.out.print("Enter n: ");
        int n = input.nextInt();

        sol.pattern(n);
    }
}