/******************************************************************************

Welcome to GDB Online.
GDB online is an online compiler and debugger tool for C, C++, Python, Java, PHP, Ruby, Perl,
C#, VB, Swift, Pascal, Fortran, Haskell, Objective-C, Assembly, HTML, CSS, JS, SQLite, Prolog.
Code, Compile, Run and Debug online from anywhere in world.

*******************************************************************************/
import java.util.*;
public class Main
{
	public static void main(String[] args) {
	    
	    Scanner sc=new Scanner(System.in);
		int n=sc.nextInt();
		int[] arr=new int[n];
		for(int i=0;i<n;i++)
		{
		    arr[i]=sc.nextInt();
		}
		
		int flag=0,p;
		for(int i=0;i<n;i++)
		{
		    p=0;
		   while(true)
		   {
		       flag=0;
		       for(int j=0;j<n;j++)
		       {
		           if(j==i)
		           {
		               continue;
		           }
		           else
		           {
		               if((arr[i]+p)%arr[j]==0)
		               {
		                   flag=0;
		               }
		               else
		               {
		                   flag=1;
		                   break;
		               }
		           }
		       }
		       if(flag==0)
		       {
		           break;
		       }
		       p++;
		       
		   }
		    if(flag==0)
		    {
		        System.out.print(p+" ");
		    }
		}
	}
	
	
	
}
