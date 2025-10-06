#include<bits/stdc++.h>
using namespace std;
class Solution
{
public:
    vector<vector<int>> countFrequencies(vector<int> &nums)
    {
        // Your code goes here
        vector<vector<int>> hash;

        for (auto &e : nums)
        {
            int found = 0;
            for (auto &j : hash)
            {
                if (j[0] == e)
                {
                    j[1]++;
                    found = 1;
                    break;
                }
            }
            if (found == 0)
            {
                hash.push_back({e, 1});
            }
        }
        return hash;
    }
};
int main()
{
    Solution obj;
    vector<int> nums = {1, 2, 2, 3, 1, 4, 4, 4};
    vector<vector<int>> result = obj.countFrequencies(nums);
    for (auto &pair : result)
    {
        cout << "[" << pair[0] << ", " << pair[1] << "] ";
    }
    return 0;
}
