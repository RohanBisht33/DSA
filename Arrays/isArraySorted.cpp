#include <iostream>
#include <vector>

using namespace std;

class Solution
{
public:
    bool isSorted(vector<int> &nums)
    {
        // your code goes here
        for (int i = 0; i < nums.size() - 1; i++)
        {
            if (nums[i] > nums[i + 1])
            {
                return false;
            }
        }
        return true;
    }
};

int main()
{
    Solution sol;
    int n;
    vector<int> nums;
    nums = {1, 2, 3, 4, 5};
    n = nums.size();

    // avoid calling isSorted on empty vector because of the loop in it
    if (n == 0)
    {
        cout << "true\n";
    }
    else
    {
        cout << (sol.isSorted(nums) ? "true\n" : "false\n");
    }

    return 0;
}