package python_is_king;

import java.util.*;

public class sanabbai {

	public static String maxElement(String input1)
	{
		Map<Character,Integer> map=new HashMap<>();
		
		for(int i=0;i<input1.length();i++)
		{
			char key=input1.charAt(i);
			if(map.containsKey(key))
			{
				int val=map.get(key);
				map.put(key,val+1);
			}
			else
			{
				map.put(key,1);
			}
		}
		
		int max=0;
		String maxc="";
		for(Map.Entry<Character, Integer> i :map.entrySet())
		{
			if(i.getValue()>max)
			{
				max=i.getValue();
				maxc="";
				maxc+=i.getKey();
			}
			
		}
		return maxc;
		
	}
	
	public static void main(String[] args) {
		
		Scanner sc=new Scanner(System.in);
		String st=sc.nextLine();
		System.out.println(maxElement(st));

	}

}
