#include <bits/stdc++.h>
using namespace std;

class Solution
{
public:
    int largestElement(vector<int> &nums)
    {
        int max_element = nums[0];

        for (int i = 1; i < nums.size(); i++)
        {
            if (nums[i] > max_element)
            {
                max_element = nums[i];
            }
        }
        return max_element;
    }
};

int main() {
    int n;
    if (!(cin >> n)) return 0;
    vector<int> nums(n);
    for (int i = 0; i < n; ++i) cin >> nums[i];

    Solution sol;
    cout << sol.largestElement(nums) << '\n';
    return 0;
}
