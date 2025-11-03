#include <iostream>
#include <vector>
using namespace std;

class Solution
{
public:
    void rotateArrayByOne(vector<int> &nums)
    {
        size_t n = nums.size();
        if (n == 0) return;

        int head = nums[0];
        for (size_t i = 0; i + 1 < n; ++i)
        {
            nums[i] = nums[i + 1];
        }
        nums[n - 1] = head;
    }
};
int main()
{
    vector<int> a;
        
    a = {1, 2, 3, 4, 5};

    Solution sol;
    sol.rotateArrayByOne(a);

    for (size_t i = 0; i < a.size(); ++i)
    {
        if (i)
            cout << ' ';
        cout << a[i];
    }
    cout << '\n';
    return 0;
}