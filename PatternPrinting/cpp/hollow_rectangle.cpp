#include <iostream>
using namespace std;

int main()
{
    int range = 10;

    for (int i = 0; i < range; i++)
    {
        for (int j = 0; j < range; j++)
        {
            if ((i != 0 && i != range - 1) && (j != 0 && j != range - 1))
            {
                cout << " ";
            }
            else
            {
                cout << "*";
            }
        }
        cout << endl;
    }

    return 0;
}