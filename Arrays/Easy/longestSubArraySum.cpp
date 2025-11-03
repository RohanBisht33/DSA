#include <bits/stdc++.h>
using namespace std;

class Solution
{
public:
    int longestSubarray(vector<int> &nums, int k)
    {
        int maxCount = 0;
        for (int i = 0; i < nums.size(); i++)
        {
            int sum = 0;
            for (int j = i; j < nums.size(); j++)
            {

                sum += nums[j];
                if (sum == k)
                {
                    maxCount = max(maxCount, j - i + 1);
                }
            }
        }
        return maxCount;
    }
};

int main(){
    int t = 3;
    while(t--){
        int size, k;
        cin >> size >> k;
        vector<int> arr(size);
        for (auto &e : arr)
        {
            cin >> e;
        }

        Solution sol;
        int result = sol.longestSubarray(arr, k);
        cout << result <<endl;
    }
}