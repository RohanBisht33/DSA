#include <iostream>
using namespace std;
class Solution
{
public:
    int GCD(int n1, int n2)
    {
        int n, prev = 1;
        if (n1 > n2)
        {
            n = n2;
        }
        else
        {
            n = n1;
        }
        for (int i = 1; i <= n; i++)
        {
            if (n1 % i == 0 && n2 % i == 0)
            {
                prev = i;
            }
        }
        return prev;
    }
};

int main()
{
    Solution sol;
    int a, b;
    cout << "Enter two numbers: ";
    cin >> a >> b;
    int result = sol.GCD(a, b);
    cout << "GCD of " << a << " and " << b << " is " << result << std::endl;
    return 0;
}