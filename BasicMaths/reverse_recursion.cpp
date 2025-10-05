#include <iostream>
using namespace std;

class Solution
{
public:
    int i = 0;
    void reverse(int arr[], int n)
    {
        int rev = arr[i];
        arr[i] = arr[n - 1];
        arr[n - 1] = rev;
        i++;
        if (i == n)
        { // RECURSION
            return;
        }
        reverse(arr, n - 1);
    }
};
// 1,2,3,4,5,6,7,8,9,10,11 => n=11
// i = 0,1,2,3,4,5,6,7,8,9
// i = 0, i<n/2 => i < 5

int main()
{
    int arr[] = {1,2,3,4,5,6,7,8,9,10,11};
    int n = sizeof(arr) / sizeof(arr[0]);
    Solution sol;
    sol.reverse(arr, n);
    cout << "Reversed array: ";
    for (int i = 0; i < n; i++)
    {
        cout << arr[i] << " ";
    }
    cout << endl;
    return 0;
}