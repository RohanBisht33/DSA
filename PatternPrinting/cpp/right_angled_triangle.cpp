#include <iostream>

int main()
{
    int row = 5;
    int column = 5;

    for (int i = 0; i < row; i++)
    {
        for (int j = 0; j < column; j++)
        {
            printf("*");
        }
        printf("\n");
    }

    return 0;
}