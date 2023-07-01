import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.StringTokenizer;

public class Main {
    static int W, H;
    static int[][] board;
    static boolean[][] visited;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        H = Integer.parseInt(st.nextToken());
        W = Integer.parseInt(st.nextToken());
        board = new int[H][W];
        visited = new boolean[H][W];

        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < W; i++) {
            int h = Integer.parseInt(st.nextToken());
            for (int j = 0; j < h; j++) {
                board[j][i] = 1;
            }
        }

        for (int i = 0; i < H; i++) {
            for (int j = 0; j < W; j++) {
                if (!visited[i][j] && board[i][j] == 0) {
                    fillWater(j, i);
                }
            }
        }

        System.out.println(getAmount());
    }

    public static void fillWater(int x, int y) {
        boolean leak = false;
        List<Integer> pos = new ArrayList<>();
        if (x == 0 && board[y][x] == 0) leak = true;
        for (int i = x; i < W; i++) {
            if (board[y][i] == 1) break;
            visited[y][i] = true;
            if (i == W - 1 && board[y][i] == 0) {
                leak = true;
                break;
            }
            pos.add(i);
        }

        if (!leak) {
            for (Integer idx : pos) {
                board[y][idx] = 2;
            }
        }
    }

    public static int getAmount() {
        int count = 0;
        for (int i = 0; i < H; i++) {
            for (int j = 0 ; j < W; j++) {
                if (board[i][j] == 2) {
                    count++;
                }
            }
        }
        return count;
    }
}
