#include<iostream>
using namespace std;
class Solution{
    public :
        int countDigit(int n){
        int count = 0;
            while (n != 0)
            {
                count++;
                n = n / 10;
            }
            return count;
        }
};
    
int main() {
    Solution sol;
    int n;
    cout << "Enter a number: ";
    cin >> n;
    int result = sol.countDigit(n);
    cout << "Number of digits: " << result << endl;
    return 0;
}