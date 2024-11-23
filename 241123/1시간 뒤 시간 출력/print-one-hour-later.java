import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner s = new Scanner(System.in);
        s.useDelimiter(":");

        int h = s.nextInt();
        h = h + 1;
        int m = s.nextInt();

        System.out.printf("%d:%d",h,m);

    }
}