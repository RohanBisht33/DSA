#include <bits/stdc++.h>
using namespace std;

class Solution
{
public:
    int removeDuplicates(vector<int> &nums)
    {
        int temp = nums[0];
        int count = 1;

        for (int i = 1; i < nums.size(); i++)
        {
            if (nums[i] == temp)
            {
                nums.erase(nums.begin() + i);
                i--;
            }
            else
            {
                temp = nums[i];
                count++;
            }
        }
        return count;
    }
};

int main() {
    Solution sol;
    vector<int> nums = {0,0,3,3,5,6,9,9};
    cout << "Before: ";
    for (int v : nums) cout << v << " ";
    cout << "\n";

    int ret = 0;
    if (!nums.empty()) ret = sol.removeDuplicates(nums);

    cout << "After (first " << ret << " elements): ";
    for (int i = 0; i < ret; ++i) cout << nums[i] << " ";
    cout << "\nReturned value: " << ret << "\n";
    return 0;
}