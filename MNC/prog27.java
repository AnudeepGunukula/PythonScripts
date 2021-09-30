package python_is_king;
import java.util.*;
public class som2 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner sc=new Scanner(System.in);
		
		int x=sc.nextInt();
		int[] candles=new int[x];
		for(int i=0;i<x;i++)
		{
			candles[i]=sc.nextInt();
		}
		int[] arr=new int[2];
		int a,b,c = 0;
		for(int i=0;i<arr.length;i++)
		{
			arr[i]=sc.nextInt();
		}
		
		int[] ans=new int[arr[0]];
		
		int[] copy=new int[candles.length];
		for(int i=0;i<arr[0];i++)
		{
			a=sc.nextInt();
			b=sc.nextInt();
			c=sc.nextInt();
			
			candles[a-1]=b;
			
			for(int s=0;s<x;s++)
			{
				copy[s]=candles[s];
			}
			
			Arrays.sort(copy);
			

			ans[i]=copy[c-1];
			
		}
		
		for(int i=0;i<ans.length;i++)
		{
			System.out.println(ans[i]);
		}
		
	}

}
