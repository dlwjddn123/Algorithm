import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {
    static char[][] board;
    static boolean[][] visited;
    static boolean[][] tempVisited;
    static int N, M;
    static char curAlpha;
    static String result = "No";
    static int[] dx = {0, 0, 1, -1};
    static int[] dy = {1, -1, 0, 0};

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());
        board = new char[N][M];
        visited = new boolean[N][M];
        for (int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine());
            String t = st.nextToken();
            for (int j = 0; j < M; j++) {
                board[i][j] = t.charAt(j);
            }
        }

        outLoop :
        for (int i = 0; i < N; i ++) {
            for (int j = 0; j < M; j++) {
                if (!visited[i][j]) {
                    tempVisited = new boolean[N][M];
                    curAlpha = board[i][j];
                    dfs(j, i, j, i);
                }
                if (result.equals("Yes")) {
                    break outLoop;
                }
            }
        }
        System.out.println(result);
    }

    public static void dfs(int curX, int curY, int preX, int preY) {
        if (tempVisited[curY][curX]) {
            result = "Yes";
            return;
        }
        for (int i = 0; i < 4; i++) {
            if (0 <= curX + dx[i] && curX + dx[i] < M && 0 <= curY + dy[i] && curY + dy[i] < N) {
                if (curAlpha == board[curY + dy[i]][curX + dx[i]] && (curX + dx[i] != preX || curY + dy[i] != preY)) {
                    tempVisited[curY][curX] = true;
                    visited[curY][curX] = true;
                    dfs(curX + dx[i], curY + dy[i], curX, curY);
                }
            }
        }
    }
}
