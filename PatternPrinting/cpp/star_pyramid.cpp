#include <iostream>
using namespace std;

int main()
{
    int rows = 5;

    for (int i = 0; i < rows; i++)
    {
        for (int j = 0; j < rows - 1 - i; j++)
        {
            cout << " ";
        }
        for (int k = 0; k < 2 * i - 1; k++)
        {
            cout << "*";
        }
        cout << endl;
    }
    // i = 0 to rows  //j = 0 to rows-i-1  //k = 0 to 2*i-1
    // i \  j  \   k
    // 0 \ 0-3 \ 1 star
    // 1 \ 0-2 \ 3 star
    // 2 \ 0-1 \ 5 star
    // 3 \ 0-0 \ 7 star

    return 0;
}