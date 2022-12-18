import java.util.Scanner;

public class Code {
    public static void main(String args[]) {
        Scanner sc = new Scanner(System.in);

        System.out.print("Name : ");
        String name = sc.nextLine();
        if (name.length() > 0) 
            System.out.printf("Hello, %s!", name);
        else
            System.out.print("Hello, SJEC!");
    }
}