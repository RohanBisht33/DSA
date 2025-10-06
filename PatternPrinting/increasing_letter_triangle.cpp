#include <iostream>
using namespace std;

int main()
{
    int rows = 5;
    for (int i = 0; i < rows; i++)
    {
        for (int j = 65; j < i + 66; j++)
        {
            cout << (char)j << " ";
        }
        cout << endl;
    }

    return 0;
}