import java.util.Scanner;
public class MainTest{
    public static void main (String[]args){
        Scanner sc = new Scanner(System.in);
        String day = sc.next();
        int num = sc.nextInt();

        Test1 test1 = new Test1(num);
        test1.ramen();

        Test2 test2 = new Test2(day, num);
        test2.ramen();

        Test1 test3 = new Test2(day, num);
        test3.ramen();
    }
}
