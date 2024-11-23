import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner s = new Scanner(System.in);

        s.useDelimiter("-");

        int m = s.nextInt();

        int d = s.nextInt();

        int y = s.nextInt();

        System.out.printf("%d.%d.%d", y,m,d);
    }
}