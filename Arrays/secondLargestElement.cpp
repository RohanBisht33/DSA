#include <bits/stdc++.h>
using namespace std;

class Solution
{
public:
    int secondLargestElement(vector<int> &nums)
    {
        int max_element = -1;
        int prev_element = -1;

        for (int i = 0; i < nums.size(); i++)
        {
            if (nums[i] > max_element)
            {
                prev_element = max_element;
                max_element = nums[i];
            }
            if (nums[i] > prev_element && nums[i] != max_element)
            {
                prev_element = nums[i];
            }
        }
        return (prev_element == max_element) ? -1 : prev_element;
    }

};

int main()
{
    int n;
    vector<int> nums;
    
    nums = {8, 8, 7, 5, 2};

    Solution sol;
    cout << sol.secondLargestElement(nums) << '\n';
    return 0;
}
