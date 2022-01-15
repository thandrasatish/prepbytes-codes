#include <stdio.h>
int main()
{
int n,t;
scanf("%d",&t);
while(t--)
{
  scanf("%d\n",&n);
  if(((n % 4 == 0) && (n % 100!= 0)) || (n%400 == 0))
  printf("Yes\n");
  else
  printf("No\n");
}
}
