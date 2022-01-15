#include <stdio.h>

int main()
{
  int t;
  scanf("%d",&t);
  while(t--)
  {
    int q,p;
    scanf("%d %d",&q,&p);
    float price=q*p;
    if(q>100)
    {
      price-=0.2*q*p;
    }
    printf("%.1f\n",price);
  }
  
  return 0;
}
