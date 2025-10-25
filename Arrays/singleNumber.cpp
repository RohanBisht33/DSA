#include <bits/stdc++.h>
using namespace std;

// class Solution{    
// public:    
//     int singleNumber(vector<int>& nums){
//         //your code goes here
//         vector<vector<int>> hash;

//         for(auto& e:nums){

//             bool found = false;
//             for(auto& n:hash){
//                 if(n[0] == e){
//                     n[1]++;
//                     found = true;
//                     break;
//                 }
//             }

//             if(found != true){
//                 hash.push_back({e,1});
//             }
//         }

//         for(auto& h:hash){
//             if(h[1] == 1){
//                 return h[0];
//             }
//         }
//     }
// };

class Solution{    
public:    
    int singleNumber(vector<int>& nums){
        int Xor = 0;
        for(int i = 0; i < nums.size(); i++){
            Xor ^= nums[i];
        }
        return Xor;
    }
};

int main(){
    int t;
    cin>>t;
    while(t--){
        int size;
        cin >> size;
        vector<int> arr(size);
        for (auto &e : arr)
        {
            cin >> e;
        }
        Solution sol;
        int result = sol.singleNumber(arr);
        cout << result <<endl;
    }
}