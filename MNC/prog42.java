package python_is_king;

import java.util.*;
public class sanabbai3 {

	public static void main(String[] args) {

		Scanner sc=new Scanner(System.in);
		
		int n=sc.nextInt();
		
		String st="PN";
		
		
		int[] arr=new int[n];
		for(int i=0;i<n;i++)
		{
			arr[i]=sc.nextInt();
		}
		
		
		
		System.out.println(findmaximum(arr,st,n));
	}

	public static int findmaximum(int[] input1, String input2, int n) {
		
		int mag=0;
		for(int i=0;i<input2.length();i++)
		{
			if(input2.charAt(i)=='P')
			{
				mag+=input1[i];
			}
			else
			{
				mag-=input1[i];
			}
		}
		
		if(mag<0)
		{
			mag=mag*(-1);
		}
		
		return mag*100;
	}

}
