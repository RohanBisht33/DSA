#include<bits/stdc++.h>
using namespace std;

class Solution
{
public:
    int missingNumber(vector<int> &nums)
    {
        int n = nums.size();
        int sum = 0;
        int sum2 = 0;
        for (int i = 0; i <=n; i++){
            sum += i;
        }
        for (int i = 0; i < nums.size(); i++)
        {
            sum2 += nums[i];
        }
        
        if(sum == sum2){
            return 0;
        }
        else{
            return sum-sum2;
        }
    }
};

int main(){
    vector<int> arr(6);
    for(auto& e:arr){
        cin >> e;
    }
    Solution sol; 
    int result = sol.missingNumber(arr);
    cout << result;
}