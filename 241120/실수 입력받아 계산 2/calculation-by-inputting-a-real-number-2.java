import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        // Scanner를 사용하여 사용자로부터 입력받기
        Scanner scanner = new Scanner(System.in);

        double a = scanner.nextDouble(); // 실수 입력 받기

        // a에 1.5를 더하기
        double result = a + 1.5;

        // 소수점 둘째 자리까지 반올림
        result = Math.round(result * 100) / 100.0;

        // 결과 출력
        System.out.println(result);

        scanner.close(); // Scanner 닫기
    }
}