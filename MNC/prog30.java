import java.util.*;


public class numbersearch
{
    public static void main(String[] args)
    {
        Scanner sc=new Scanner(System.in);

        String st=sc.nextLine();
        double count=0, letter=0;
        for(int i=0;i<st.length();i++)
        {
            if(Character.isDigit(st.charAt(i)))
            {
                count+=Character.getNumericValue(st.charAt(i));  
            }
            else if(Character.isLetter(st.charAt(i)))
            {
                letter+=1;
            }
        }

        double x=count/letter;
        double ans=Math.rint(x);
        System.out.print((int)ans);


    }
}
