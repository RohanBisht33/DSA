#include <bits/stdc++.h>
using namespace std;

class Solution
{
public:
    void merge(vector<int> &nums1, vector<int> &nums2, vector<int> &arr)
    {
        int left = 0, right = 0;

        while (left < nums1.size() && right < nums2.size())
        {
            if (nums1[left] == nums2[right])
            {
                if (arr.empty() || arr.back() != nums1[left])
                    arr.push_back(nums1[left]);
                left++;
                right++;
            }
            else if (nums1[left] < nums2[right])
            {
                if (arr.empty() || arr.back() != nums1[left])
                    arr.push_back(nums1[left]);
                left++;
            }
            else
            {
                if (arr.empty() || arr.back() != nums2[right])
                    arr.push_back(nums2[right]);
                right++;
            }
        }

        while (left < nums1.size())
        {
            if (arr.empty() || arr.back() != nums1[left])
                arr.push_back(nums1[left]);
            left++;
        }
        while (right < nums2.size())
        {
            if (arr.empty() || arr.back() != nums2[right])
                arr.push_back(nums2[right]);
            right++;
        }
    }

    vector<int> unionArray(vector<int> &nums1, vector<int> &nums2)
    {
        sort(nums1.begin(), nums1.end()); // ensure sorted
        sort(nums2.begin(), nums2.end()); // ensure sorted
        vector<int> arr;
        merge(nums1, nums2, arr);
        return arr;
    }
};

int main()
{
    vector<int> nums1(6), nums2(5);

    for (int &x : nums1)
        cin >> x;
    for (int &x : nums2)
        cin >> x;

    Solution sol;
    vector<int> arr = sol.unionArray(nums1, nums2);

    for (auto &e : arr)
        cout << e << " ";
    cout << endl;

    return 0;
}
