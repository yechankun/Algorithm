#include<iostream>
using namespace std; 
int main(){
    int a, b;
    cin>>a;
    if(a>89)
        cout<<"A"<<endl;
    else if(a>79)
        cout<<"B"<<endl;
    else if(a>69)
        cout<<"C"<<endl;
    else if(a>59)
        cout<<"D"<<endl;
    else
        cout<<"F";
}