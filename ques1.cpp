#include<bits/stdc++.H>
using namespace std;

int main()
{
    int num;
    cout<<"Enter 3-digit num: ";
    cin>>num;
    int sum=0;
    while(n!=0)
    {
        int rem=num%10;
        sum = sum*10 + rem;
        num/=10;
    }
    cout<<sum<<endl; 
    cout<<endl;
}   