import java.util.*;
public class internal {
    public static void main(String[] args) {


        Scanner scn=new Scanner(System.in);
        int n = scn.nextInt();

        String a[] = new String[n];

        String k = "", kk = "";
        ;

        for (int i = 0; i < n; i++)

        {

            a[i] = scn.nextLine();

        }

        for (int i = 0; i < n; i++)

        {

            String z[] = a[i].split(" ");

            if (Integer.parseInt(z[0]) == 1)

            {

                kk = k;

                k = k + z[1];

            }

            else if (Integer.parseInt(z[0]) == 2)

            {

                kk = k;

                k = k.substring(0, k.length() - Integer.parseInt(z[1]));

            }

            else if (Integer.parseInt(z[0]) == 3)

            {

                System.out.println(k.charAt(Integer.parseInt(z[1])));

            }

            else if (Integer.parseInt(z[0]) == 4)

            {

                k = kk;

            }

        }
    }
}
