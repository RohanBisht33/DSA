#include <iostream>
#include <vector>
using namespace std;

class Solution
{
public:
    void insertion_Sort(vector<int> &nums, int key, int n)
    {
        int j = key - 1;
        if (key >= n)
        {
            return;
        }
        if (j < 0)
        {
            insertion_Sort(nums, key + 1, n);
            return;
        }
        if (nums[j] > nums[key])
        {
            nums[j + 1] = nums[j];
            j--;
        }
        nums[j + 1] = nums[key];
        insertion_Sort(nums, key, n);
    }
    vector<int> insertionSort(vector<int> &nums)
    {
        size_t n = nums.size();
        int key = 1;

        insertion_Sort(nums, key, n);
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
