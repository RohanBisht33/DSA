#include <iostream>
using namespace std;

int main()
{
    int rows = 4;
    for (int i = 2; i < rows + 2; i++)
    {
        for (int j = 1; j < i; j++)
        {
            cout << j;
        }
        for (int j = 0; j < 2 * rows - 2 * i + 2; j++)
        {
            cout << " ";
        }
        for (int j = i - 1; j >= 1; j--)
        {
            cout << j;
        }
        cout << endl;
    }

    return 0;
}