#include <iostream>
using namespace std;

int main()
{
    int range = 9;

    for (int i = range / 2; i >= 0; i--)
    {
        for (int j = 0; j <= range / 2 - i; j++)
        {
            cout << "*";
        }
        for (int j = 2 * i; j > 0; j--)
        {
            cout << " ";
        }
        for (int j = range / 2 - i + 1; j > 0; j--)
        {
            cout << "*";
        }

        cout << endl;
    }

    for (int i = 0; i <= range / 2; i++)
    {
        for (int j = 0; j < range / 2 - i; j++)
        {
            cout << "*";
        }
        for (int j = 0; j < 2 * i + 2; j++)
        {
            cout << " ";
        }
        for (int j = range / 2 - i; j > 0; j--)
        {
            cout << "*";
        }

        cout << endl;
    }

    return 0;
}