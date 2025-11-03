#include <bits/stdc++.h>
using namespace std;

class Solution
{
public:
    vector<int> twoSum(vector<int> &nums, int target)
    {
        unordered_map<int, int> hash;
        for (int i = 0; i < nums.size(); i++)
        {
            int need = target - nums[i];
            if (hash.find(need) != hash.end())
            {
                return {hash[need], i};
            }
            hash[nums[i]] = i;
        }
        return {-1, -1};
    }
};
// Time Complexity: O(n)

int main()
{
    Solution sol;
    vector<int> nums(5);
    int target;
    for (auto& num: nums){
        cin >> num;
    }
    cin >> target;
    vector<int> result = sol.twoSum(nums, target);
    cout << "Indices: " << result[0] << ", " << result[1] << endl;
    return 0;
}