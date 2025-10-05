#include <iostream>
using namespace std;

class Solution{	
    public:
        int NnumbersSum(int N){
            if(N == 0){
                return 0;
            }
            return N + NnumbersSum(N-1);
        }
};

int main() {
    int N;
    cout << "Enter N: ";
    cin >> N;
    Solution sol;
    cout << "Sum of first " << N << " natural numbers is: " << sol.NnumbersSum(N) << endl;
    return 0;
}