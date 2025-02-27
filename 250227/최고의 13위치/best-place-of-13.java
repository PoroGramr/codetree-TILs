import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int [][] town = new int[n][n];

        for(int i = 0 ;i < n; i++){
            for(int k=0; k<n;k++){
                town[i][k] = sc.nextInt();
            }
        }
        int maxCnt = 0;

        for(int i = 0 ;i < n; i++){
            for(int k=0; k< n - 2;k++){
                maxCnt = Math.max(maxCnt, town[i][k] + town[i][k+1]+town[i][k+2]);
            }
        }
        System.out.print(maxCnt);

    }
}