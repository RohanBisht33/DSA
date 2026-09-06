#include <iostream>
using namespace std;

int main()
{
    
    int rows = 5;
    for (int i = 0; i < rows; i++){
        for(int j = 0; j < rows-i-1; j++){
            cout<<" ";
        }
        
        for(int j = 0; j < 2*i+1; j++){
            cout<<"*";
        }
        cout<<endl;
    }
    for (int i = rows; i > 0; i--){
        for(int j = rows-i; j > 0; j--){
            cout<<" ";
        }
        for(int j = 2*i-1; j > 0; j--){
            cout<<"*";
        }
        cout<<endl;
    }
    return 0;
}
