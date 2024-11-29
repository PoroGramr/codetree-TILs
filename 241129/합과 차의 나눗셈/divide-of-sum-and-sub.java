import java.util.Scanner;

public class Main {


    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        // 두 정수를 입력받기
        int a = scanner.nextInt();

        int b = scanner.nextInt();

        // 합과 차 계산
        int sum = a + b;
        int difference = a - b;

        double result = (double) sum / difference;
        System.out.printf("%.2f\n", result);

    }
}