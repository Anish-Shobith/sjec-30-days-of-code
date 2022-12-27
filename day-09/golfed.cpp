#include <iostream>
using namespace std;main(){int n,i,j=0;cin>>n;for(i=0;i<n;i++){string s;for(j=0;j<i+1;j++)s+="# ";cout<<string(n-i-1,' ')<<s<<"\n";}for(i=0;i<n;i++){string s;for(j=0;j<n-i-1;j++)s+="# ";cout<<string(i+1,' ')<<s<<"\n";}}
