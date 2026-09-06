#include <iostream>
using namespace std;

int main()
{
    int rows = 4;
    for (int i = 0; i < rows; i++)
    {
        for (int j = 0; j < rows - i - 1; j++)
        {
            cout << " ";
        }
        for (int j = 0; j < i + 1; j++)
        {
            cout << char(j + 65);
        }
        for (int k = i; k > 0; k--)
        {
            cout << char(k + 64);
        }
        cout << endl;
    }

    return 0;
}