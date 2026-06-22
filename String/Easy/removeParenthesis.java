import java.util.Scanner;

class Solution {
    public String func(String s) {
        // Your code goes here
        left = 0;
        right = s.length()-1;
        for(int i = 0; i < s.length(); i++){
            if(str[i]){
                func()
            }
        }
        return s;
    }
}

public class removeParenthesis {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        Solution sol = new Solution();

        System.out.print("Enter an input: ");
        String str = input.next();

        String output = sol.func(str);

        System.out.println("Output: " + output);
    }
}