#include<bits/stdc++.h>
using namespace std;

class Solution {
public:
    void sortZeroOneTwo(vector<int>& nums) {
        int low = 0;
        int mid = 0;
        int high = (int)nums.size() - 1;
        while (mid <= high) {
            if (nums[mid] == 0) {
                swap(nums[low], nums[mid]);
                low++;
                mid++;
            } else if (nums[mid] == 1) {
                mid++;
            } else { // nums[mid] == 2
                swap(nums[mid], nums[high]);
                high--;
            }
        }
    }
};

int main(){
    int t;
    cin>>t;
    while(t--){
        int n;
        cin >> n;
        vector<int> arr(n);
        for (auto& a : arr){
            cin >> a;
        }
        Solution sol;
        sol.sortZeroOneTwo(arr);

        for(auto& a: arr){
            cout << a;
        }
        cout<<endl;
    }
}