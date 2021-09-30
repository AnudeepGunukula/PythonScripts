package python_is_king;
import java.util.Scanner;

public class som {

	public static void main(String[] args) {

		Scanner sc=new Scanner(System.in);
		int arr[]=new int[2];
		for(int i=0;i<2;i++)
		{
			arr[i]=sc.nextInt();
		}
		int x=arr[1];
		int ans=0;
		int pages[]=new int[x];
		
		for(int i=0;i<arr[1];i++)
		{
			int page=sc.nextInt();
			pages[i]=page%10;
			if(i==0 || pages[i]==0)
			{
				ans+=pages[i];
			}
			else
			{
				ans*=pages[i];
			}
		}
		
		double m=Math.pow(10,9);
		m=m+7;
		ans=(int) (ans % m);
		System.out.println(ans);

	}

}
