#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int linearSearch(vector<int>& nums, int target) {
        //your code goes here
        int count = 0;
        for(int i = 0; i <nums.size(); i++){
            if(nums[i] == target){
                return count;
            }
            count++;
        }
        return -1;
    }
};

int main() {
    Solution sol;
    vector<int> nums = {0,0,3,3,5,6,9,9};
    int target = 5;
    int ret = sol.linearSearch(nums,target);
    cout << "Index: " << ret << "\n";
    return 0;
}