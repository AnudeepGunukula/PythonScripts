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
		int[] cpy=new int[n];
		for(int i=0;i<n;i++)
		{
		    arr[i]=sc.nextInt();
		    cpy[i]=arr[i];
		}
		Arrays.sort(cpy);
		for(int i=0;i<n;i++)
		{
		    if(arr[i]!=cpy[i])
		        {
		            System.out.print(i+" ");
		        }
		}
		
	}
	
	
	
}
