#include <iostream>
using namespace std;

int main()
{
    // i = rows to 0  //j = rows-i-1 to 0  //k = 2*i-1 to 0
    // i \  j  \   k
    // 3 \ 0-0 \ 7 star
    // 2 \ 0-1 \ 5 star
    // 1 \ 0-2 \ 3 star
    // 0 \ 0-3 \ 1 star

    int rows = 5;

    for (int i = rows; i > 0; i--)
    {
        for (int j = rows - i; j > 0; j--)
        {
            cout << " ";
        }
        for (int j = 2 * i - 1; j > 0; j--)
        {
            cout << "*";
        }
        cout << endl;
    }
    return 0;
}
