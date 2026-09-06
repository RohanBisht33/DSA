import java.util.Scanner;
 
class Solution {
    public void pattern(int n) {

        for(int i = n; i>0; i--){
            for(int j = 1; j <i+1; j++){
                System.out.print(j);
            }
            System.out.println("");
        }
        
    }
}

public class upside_down_right_angled_series {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        Solution sol = new Solution();

        System.out.println("Enter n: ");
        int n = input.nextInt();

        sol.pattern(n);
    }
}