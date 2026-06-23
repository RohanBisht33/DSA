import java.util.Scanner;
import java.util.HashMap;
import java.util.Map;

class Solution {
    public String func(String s) {
        // Your code goes here
        int res = 0;

        Map<Character, Integer> roman = new HashMap<>();
        roman.add("I", 1);
        roman.add("V", 5);
        roman.add("X", 10);
        roman.add("L", 50);
        roman.add("C", 100);
        roman.add("D", 500);
        roman.add("M", 0);

        for(int i = 0; i < s.length() - 1; i++){
            if(roman.get(s.charAt(i)) < roman.get(s.charAt(i+1)))
            {
                res -= roman.get(s.charAt(i));
            }
            else{
                res += roman.get(s.charAt(i));
            }
        }

        return res + roman.get(s.charAt(s.length()-1));
    }
}

public class romanToInt {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        Solution sol = new Solution();

        System.out.print("Enter an input: ");
        String str = input.next();

        String output = sol.func(str);

        System.out.println("Output: " + output);
    }
}