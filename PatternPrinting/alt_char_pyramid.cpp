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
        for (int j = 0; j < 2 * i + 1; j++)
        {
            if (j % 2 != 0)
            {
                cout << char(66);
            }
            else
            {
                cout << char(65);
            }
        }
        cout << endl;
    }

    return 0;
}