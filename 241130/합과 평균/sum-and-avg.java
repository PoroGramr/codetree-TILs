import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner s = new Scanner(System.in);

        int a = s.nextInt();
        int b = s.nextInt();

        int c = a + b;

       double average = (double) c / 2;

        // 결과 출력
        System.out.printf("%d %.1f\n", c, average);
    }
}
