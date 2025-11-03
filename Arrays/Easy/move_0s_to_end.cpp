#include <bits/stdc++.h>
using namespace std;

class Solution
{
public:
    void moveZeroes(vector<int> &nums)
    {
        int j = 0;
        for (int i = 0; i < nums.size(); i++)
        {
            if (nums[i] != 0)
            {
                swap(nums[i], nums[j]);
                j++;
            }
            
        }
    }
};

int main(){
    vector<int> arr(6);
    for (int i = 0; i < arr.size(); i++)
    {
        cin >> arr[i];
    }

    for (auto &e : arr)
    {
        cout << e;
    }
    cout << endl;
    Solution sol;
    sol.moveZeroes(arr);

    for(auto& e: arr){
        cout<<e;
    }
    cout<< endl;
}