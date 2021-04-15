#include<iostream>
using namespace std; 
int main(){
    double a, b;
    cin>>a>>b;
    if(b<45){
        if(a<1){
            a=23; b=b+60-45;
        }
        else{ a=a-1; b=b+60-45;}
    }
    else b=b-45;
    cout<<a<<" "<<b;
    
}