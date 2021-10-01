package python_is_king;
import java.util.*;

class orphan
{
	
	static boolean allequal(int[] arr)
	{
		int flag=0;
		for(int i=0;i<arr.length;i++)
		{
			if(arr[i]==arr[0])
			{
				flag=1;
			}
			else
			{
				flag=0;
				break;
			}
		}
		if(flag==0) return false;
		else return true;
	}
	
    public static void main (String[] args)
    {
    	Scanner sc=new Scanner(System.in);
    	int x=sc.nextInt();
        int arr[]=new int[x];
        
        for(int i=0;i<x;i++)
        {
        	arr[i]=sc.nextInt();
        }
        Arrays.sort(arr);
        int count=0,i=0,flag=0;
        boolean boo=true;
        
        if(allequal(arr))
        {
        	count=0;
        	flag=1;
        	boo=false;
        }
        
        int big=arr.length-1;
        
        
        while(boo)
        {
        	if(count>arr.length)
        	{
        		break;
        	}
        	arr[i]+=1;
        	arr[big]-=1;
        	if(arr[big]<=1)
        	{
        		count++;
        		if(allequal(arr))
        		{
        			flag=1;
        			break;
        		}
        		else
        		{
        			flag=0;
        		}
        	}
        	i++;
        	if(i%big==0)
        	{
        		i=0;
        	}
        	count++;
        	if(allequal(arr))
        	{
        		flag=1;
        		break;
        	}
        }
       
        if(flag==1)
        System.out.println(count);
        else
        System.out.println(-1);
    }
}
