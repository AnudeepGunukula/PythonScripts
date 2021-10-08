package python_is_king;

import java.util.*;

public class sanabbai2 {
	public static int majority(int input1,int[] input2)
	{
		Map<Integer,Integer> map=new HashMap<>();
		for(int i=0;i<input1;i++)
		{
			int key=input2[i];
			
			if(map.containsKey(key))
			{
				int val=map.get(key);
				map.put(key,val+1);
			}
			else
			{
				map.put(key,1);
			} }
		int max=0;
		int maxk=0;
		int half=input1/2;
		for(Map.Entry<Integer, Integer> i :map.entrySet())
		{
			if(i.getValue()>=half)
			{
				max=i.getValue();
				maxk=i.getKey();
			}
		}
		int count=0;
		for(Map.Entry<Integer, Integer> i:map.entrySet())
		{
			if(i.getValue()==max)
			{ count+=1; }
		}
		if(count>1)
		{
			return -1;
		}
		return maxk;
	}
	
	
	public static void main(String[] args) {
 
		 Scanner sc=new Scanner(System.in);
		 
		 int n=sc.nextInt();
		 int arr[]=new int[n];
		 for(int i=0;i<n;i++)
		 {
			 arr[i]=sc.nextInt();
		 }
		 
		 System.out.println(majority(n,arr));
	}

}
