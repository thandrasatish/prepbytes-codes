import java.util.*;
import java.io.*;
public class Main {
  public static void main(String args[]) throws IOException
  {
    long t,n;
    int i;
  Scanner s=new Scanner(System.in);
  t=s.nextLong();
  while(t-->0)
  {
    n=s.nextLong();
    if(n%4==0 && (n%100!=0 || n%400==0))
    System.out.print("Yes");
    else
    System.out.print("No");
    System.out.println();
  }
    
  }
}
