#include <iostream>
#include <vector>
using namespace std;

class Solution
{
public:
    vector<int> insertionSort(vector<int> &nums)
    {
        for (int i = 1; i < nums.size(); i++)
        {
            int key = nums[i];
            int j = i - 1;
            while (j >= 0 && nums[j] > key)
            {
                nums[j + 1] = nums[j];
                j--;
            }
            nums[j + 1] = key;
        }
        return nums;
    }
};

int main()
{
    vector<int> nums = {5, 2, 9, 1, 5, 6};
    Solution sol;
    vector<int> sorted = sol.insertionSort(nums);

    for (int num : sorted)
        cout << num << " ";
    cout << endl;
    return 0;
}
