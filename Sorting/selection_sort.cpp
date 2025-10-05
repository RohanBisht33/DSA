#include <iostream>
#include <vector>
using namespace std;

class Solution
{
public:
    vector<int> selectionSort(vector<int> &nums)
    {
        for (int i = 0; i < nums.size() - 1; i++)
        {
            int min = i;
            for (int j = i + 1; j < nums.size(); j++)
            {
                if (nums[min] > nums[j])
                {
                    min = j;
                }
            }
            int temp = nums[i];
            nums[i] = nums[min];
            nums[min] = temp;
        }
        return nums;
    }
};

int main()
{
    vector<int> nums = {4, 2, 8, 6, 9};
    Solution sol;
    vector<int> sorted = sol.selectionSort(nums);

    cout << "Sorted array: ";
    for (int num : sorted)
        cout << num << " ";
    cout << endl;

    return 0;
}
