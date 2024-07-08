import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());
        long[][] board = new long[N][N];
        long[][] prefixSum = new long[N][N];

        for (int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < N; j++) {
                board[i][j] = Long.parseLong(st.nextToken());
                if (i == 0 && j == 0) {
                    prefixSum[i][j] = board[i][j];
                } else if (i == 0) {
                    prefixSum[i][j] = board[i][j] + prefixSum[i][j - 1];
                } else if (j == 0) {
                    prefixSum[i][j] = board[i][j] + prefixSum[i - 1][j];
                } else {
                    prefixSum[i][j] = board[i][j] + prefixSum[i][j - 1] + prefixSum[i - 1][j] - prefixSum[i - 1][j - 1];
                }
            }
        }
        for (int i = 0; i < M; i++) {
            st = new StringTokenizer(br.readLine());
            int y1 = Integer.parseInt(st.nextToken()) - 1;
            int x1 = Integer.parseInt(st.nextToken()) - 1;
            int y2 = Integer.parseInt(st.nextToken()) - 1;
            int x2 = Integer.parseInt(st.nextToken()) - 1;
            if (x1 == 0 && y1 == 0) {
                System.out.println(prefixSum[y2][x2]);
            } else if (x1 == 0) {
                System.out.println(prefixSum[y2][x2] - prefixSum[y1 - 1][x2]);
            } else if (y1 == 0) {
                System.out.println(prefixSum[y2][x2] - prefixSum[y2][x1 - 1]);
            } else {
                System.out.println(prefixSum[y2][x2] - prefixSum[y1 - 1][x2] - prefixSum[y2][x1 - 1] + prefixSum[y1 - 1][x1 - 1]);
            }
        }
    }
}
