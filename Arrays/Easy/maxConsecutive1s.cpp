#include <bits/stdc++.h>
using namespace std;

class Solution
{
public:
    int findMaxConsecutiveOnes(vector<int> &nums)
    {
        int prev = 0, count = 0;
        for (auto &e : nums)
        {
            if (e == 1)
            {
                count++;
            }
            else{
                prev = count;
                count = 0;
            }
        }
        return max(prev, count);
    }
};

int main(){
    int t;
    cin>>t;
    while(t--){
        vector<int> arr(8);
        for (auto &e : arr)
        {
            cin >> e;
        }
        Solution sol;
        int result = sol.findMaxConsecutiveOnes(arr);
        cout << result <<endl;
    }
}