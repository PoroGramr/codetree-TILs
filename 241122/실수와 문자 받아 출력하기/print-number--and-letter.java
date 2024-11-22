import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner s = new Scanner(System.in);

        String a = s.next();

        double b = s.nextDouble();

        double c = s.nextDouble();

        System.out.println(a);
        b = Math.round(b * 100) / 100.0;
        System.out.printf("%.2f\n", b);
        c = Math.round(c * 100) / 100.0;
        System.out.printf("%.2f", c);

        
    }
}