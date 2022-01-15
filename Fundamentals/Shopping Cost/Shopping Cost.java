import java.util.*;
import java.io.*;
public class Main {
  public static void main(String args[]) throws IOException 
  {
    int n,i,a,b;
    Scanner s = new Scanner(System.in);
    n=s.nextInt();
    for(i=1;i<=n;i++)
    {
      a=s.nextInt();
      b=s.nextInt();
      float price=a*b,p;
      if(a>100)
      {
       System.out.println(price-(0.2*a*b));
      }
      else
      System.out.println(price);
     
    }
    
    
  }
}
