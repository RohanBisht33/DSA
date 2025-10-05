#include <iostream>
using namespace std;

class Solution
{
public:
    int i = 0;
    bool palindromeCheck(string &s)
    {
        if (i >= s.length() / 2)
            return true;
        if (s[i] != s[s.length() - i - 1])
            return false;
        i++;
        return palindromeCheck(s);
    }
};

int main()
{
    Solution sol;
    string str = "imli";
    if (sol.palindromeCheck(str))
        cout << str << " is a palindrome." << endl;
    else
        cout << str << " is not a palindrome." << endl;
    return 0;
}