#include <iostream>
using namespace std;

int main()
{
    int rows = 5;
    int num = 1;
    for (int i = 0; i < rows; i++)
    {
        for (int j = 1; j < i + 2 && num <= 15; j++)
        {
            cout << num << " ";
            num++;
        }
        cout << endl;
    }

    return 0;
}