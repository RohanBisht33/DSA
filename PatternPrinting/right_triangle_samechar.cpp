#include <iostream>
using namespace std;

int main()
{
    int rows = 5;
    for (int i = 0; i < rows; i++)
    {
        for (int j = 1; j < i + 2; j++)
        {
            cout << char(i + 65) << " ";
        }
        cout << endl;
    }

    return 0;
}