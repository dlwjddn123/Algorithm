import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

public class Main {
    static char[][] board;
    static int N;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        N = Integer.parseInt(br.readLine());
        board = new char[N][N];
        char temp;
        List<Integer> result = new ArrayList<>();
        for (int i = 0; i < N; i++) {
            board[i] = br.readLine().toCharArray();
        }
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) {
                temp = board[i][j];
                result.add(findMax(i, j));
                if (j < N-1) {
                    board[i][j] = board[i][j + 1];
                    board[i][j + 1] = temp;
                    int v1 = findMaxByColumn(i, j);
                    result.add(v1);
                    board[i][j + 1] = board[i][j];
                    board[i][j] = temp;
                }

                if (i < N-1) {
                    board[i][j] = board[i + 1][j];
                    board[i + 1][j] = temp;
                    int v2 = findMaxByRow(i, j);
                    result.add(v2);
                    board[i + 1][j] = board[i][j];
                    board[i][j] = temp;
                }
            }
        }
        System.out.println(Collections.max(result));
    }

    public static int findMaxByColumn(int y, int x) {
        int Max = 0;
        int count;
        for (int i = 0; i < 2; i++) {
            count = 1;
            for (int j = 0; j < N - 1; j++) {
                if (board[j][x + i] == board[j + 1][x + i]) {
                    count += 1;
                    continue;
                }
                if (Max < count) {
                    Max = count;
                }
                count = 1;
            }
            if (Max < count) {
                Max = count;
            }
        }
        count = 1;
        for (int k = 0; k < N - 1; k++) {
            if (board[y][k] == board[y][k + 1]) {
                count += 1;
                continue;
            }
            if (Max < count) {
                Max = count;
            }
            count = 1;
        }
        if (Max < count) {
            Max = count;
        }
        return Max;
    }

    public static int findMaxByRow(int y, int x) {
        int Max = 0;
        int count;
        for (int i = 0; i < 2; i++) {
            count = 1;
            for (int j = 0; j < N - 1; j++) {
                if (board[y + i][j] == board[y + i][j + 1]) {
                    count += 1;
                    continue;
                }
                if (Max < count) {
                    Max = count;
                }
                count = 1;
            }
            if (Max < count) {
                Max = count;
            }
        }
        count = 1;
        for (int k = 0; k < N - 1; k++) {
            if (board[k][x] == board[k + 1][x]) {
                count += 1;
                continue;
            }
            if (Max < count) {
                Max = count;
            }
            count = 1;
        }
        if (Max < count) {
            Max = count;
        }
        return Max;
    }

    public static int findMax(int x, int y) {
        int Max = 0;
        int count = 1;
        for (int j = 0; j < N - 1; j++) {
            if (board[y][j] == board[y][j + 1]) {
                count += 1;
                continue;
            }
            if (Max < count) {
                Max = count;
            }
            count = 1;
        }
        if (Max < count) {
            Max = count;
        }
        count = 1;
        for (int k = 0; k < N - 1; k++) {
            if (board[k][x] == board[k + 1][x]) {
                count += 1;
                continue;
            }
            if (Max < count) {
                Max = count;
            }
            count = 1;
        }
        if (Max < count) {
            Max = count;
        }
        return Max;
    }
}
