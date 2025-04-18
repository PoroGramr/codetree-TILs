import java.util.*;
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String word1 = sc.next();
        String word2 = sc.next();
        
        char[] wordC1 = word1.toCharArray();
        char[] wordC2 = word2.toCharArray();

        Arrays.sort(wordC1);
        Arrays.sort(wordC2);
        if(wordC1.length != wordC2.length){
            System.out.print("No");
            return;
        }

        for(int i = 0; i < word1.length();i++){
            if(wordC1[i] != wordC2[i]){
                System.out.print("No");
                return;
            }
        }

        System.out.print("Yes");
        
    }
}