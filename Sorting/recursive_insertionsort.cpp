#include <iostream>
#include <vector>
using namespace std;

class Solution
{
public:
    void insertRec(vector<int> &nums, int j, int keyVal)
    {
        if (j < 0 || nums[j] <= keyVal)
        {
            nums[j + 1] = keyVal;
            return;
        }
        nums[j + 1] = nums[j];
        insertRec(nums, j - 1, keyVal);
    }

    void insertion_Sort(vector<int> &nums, int key, int n)
    {
        if (key >= n) return;
        int keyVal = nums[key];
        insertRec(nums, key - 1, keyVal);
        insertion_Sort(nums, key + 1, n);
    }

    vector<int> insertionSort(vector<int> &nums)
    {
        int n = static_cast<int>(nums.size());
        insertion_Sort(nums, 1, n);
        return nums;
    }
};

int main()
{
    vector<int> nums = {64, 34, 25, 12, 22, 11, 90};
    Solution s;
    vector<int> sorted = s.insertionSort(nums);
    for (int v : sorted)
    {
        cout << v << ' ';
    }
    cout << '\n';
    return 0;
}
