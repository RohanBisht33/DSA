#include <iostream>
#include <vector>
using namespace std;

class Solution
{
public:
    void rotateArray(vector<int> &nums, int k)
    {
        k = k % nums.size();
        if (k == 0)
        {
            return;
        }
        vector<int> temp(k);
        for (int i = 0; i < k; i++)
        {
            temp[i] = nums[i];
        }
        for (size_t i = 0; i < (nums.size() - k); i++)
        {
            nums[i] = nums[i + k];
        }
        for (size_t i = 0; i < temp.size(); i++)
        {
            nums[i + nums.size() - k] = temp[i];
        }
    }
};

int main()
{
    vector<int> a;

    a = {3, 4, 1, 5, 3, -5};
    int n = 8;
    Solution sol;
    sol.rotateArray(a,n);

    for (int i = 0; i < a.size(); i++)
    {
        cout << a[i];
    }
    cout << '\n';
    return 0;
}