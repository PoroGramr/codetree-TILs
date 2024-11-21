import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner s = new Scanner(System.in);

        double a = s.nextDouble();
        double b = s.nextDouble();
        double c = s.nextDouble();

        a = Math.round(a * 1000) / 1000.0;
        b = Math.round(b * 1000) / 1000.0;
        c = Math.round(c * 1000) / 1000.0;

        System.out.printf("%.3f\n",a);
        System.out.printf("%.3f\n",b);
        System.out.printf("%.3f",c);
         
    }
}