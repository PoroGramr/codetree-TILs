import java.util.*;
import java.io.*;

public class Main {
    static String[][] grid;
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine(), " ");

        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());

        grid = new String[n][m];

        for(int i = 0 ; i < n; i++){
            st = new StringTokenizer(br.readLine(), " ");
            for(int j = 0; j < m;j++){
                grid[i][j] = st.nextToken();
            }
        }

        int cnt = 0;
        for(int i = 1; i < n; i++)
            for(int j = 1; j < m; j++)
                for(int k = i + 1; k < n - 1; k++)
                    for(int l = j + 1; l < m - 1; l++){
                        // 그 중 색깔이 전부 달라지는 경우에만 개수를 세줍니다.
                        if(grid[0][0] != grid[i][j] && 
                           grid[i][j] != grid[k][l] &&
                           grid[k][l] != grid[n - 1][m - 1])
                            cnt++;
                    }
        System.out.println(cnt);
        }
}
