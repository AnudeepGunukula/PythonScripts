import java.util.*;
class Main
{


    public static int getDecimal(int binary)
    {  
        int decimal = 0;  
        int n = 0;  
        while(true){  
          if(binary == 0)
          {  
            break;  
          } 
          else
           {  
              int temp = binary%10;  
              decimal += temp*Math.pow(2, n);  
              binary = binary/10;  
              n++;  
           }  
        }  
        return decimal;  
    }  
   public static void main(String[] args)
   {
       Scanner sc=new Scanner(System.in);

       int x=sc.nextInt();
       int y=sc.nextInt();
       int max=0,ind=0;
       
       int[] arr=new int[x];
       for(int i=0;i<x;i++)
       {
          int n=sc.nextInt();
          n=getDecimal(n);
          arr[i]=n;
          if(n>max)
          {
              max=n;
              ind=i;
          }
          
       }

       System.out.println(ind+1);
   }
}


