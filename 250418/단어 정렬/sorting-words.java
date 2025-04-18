import java.util.*;
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        String[] wordList = new String[n];
        for (int i = 0; i < n; i++) {
            wordList[i] = sc.next();
        }
        Arrays.sort(wordList);

        for(int j = 0; j < n; j++){
            System.out.println(wordList[j]);
        }
    }
}