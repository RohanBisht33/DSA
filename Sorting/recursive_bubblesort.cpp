#include <iostream>
#include <vector>
using namespace std;

class Solution
{
public:
    void bubble_sort(vector<int> &nums, int j, int n)
    {
        if (n == 1)
        {
            return;
        }
        if (j == n - 1)
        {
            bubble_sort(nums, 0, n - 1);
            return;
        }
        if (nums[j] > nums[j + 1])
        {
            swap(nums[j], nums[j + 1]);
        }
        bubble_sort(nums, j + 1, n);
    }
    vector<int> bubbleSort(vector<int> &nums)
    {
        size_t n = nums.size();
        bubble_sort(nums, 0, n);
        return nums;
    }
};

int main() {
    vector<int> nums = {64, 34, 25, 12, 22, 11, 90};
    Solution s;
    vector<int> sorted = s.bubbleSort(nums);
    for (int v : sorted) {
        cout << v << ' ';
    }
    cout << '\n';
    return 0;
}
