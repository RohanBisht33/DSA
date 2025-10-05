#include <iostream>
#include <vector>
#include <map>
using namespace std;

class Solution
{
public:
    int mostFrequentElement(vector<int> &nums)
    {
        map<int,int> hash;
        int max_value = 0;
        int max_element;

        // Hashing
        for (auto &e : nums)
        {
            hash[e]++;
        }

        // Comparing
        for (auto& i : hash)
        {
            if (i.second > max_value)
            {
                max_value = i.second;
                max_element = i.first;
            }
        }

        return max_element;
    }
};

int main() {
    vector<int> nums = {10,9,7};
    Solution sol;
    int result = sol.mostFrequentElement(nums);
    cout << "Most frequent element: " << result << endl;
    return 0;
}
