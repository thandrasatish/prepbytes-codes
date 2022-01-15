#include <stdio.h>
int main()
{
  int n,t,i,sum=0;
  scanf("%d",&t);
  while(t--)
  {
    scanf("%d",&n);
    sum=0;
    for(i=1;i<n;i++)
    {
      if(n%i==0)
      sum=sum+i;
    }
   if(sum == n)
   printf("true\n");
   else
   printf("false\n");
  }
}
