#include<stdio.h>
int i=0,n,a[9999],s;
int main(){scanf("%d",&n);
for(;i<n;i++)scanf("%d",&a[i]),s+=a[i];
for(i=0;i<n;i++)if(a[i]>s/(float)n)printf("%d ",a[i]);}