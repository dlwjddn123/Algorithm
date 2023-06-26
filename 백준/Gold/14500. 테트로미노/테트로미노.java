import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    static List<int[][]> shapes = new ArrayList<>();
    static List<Integer> scores = new ArrayList<>();
    static int[][] board;
    static int N, M;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());
        board = new int[N][M];

        for (int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < M; j++) {
                board[i][j] = Integer.parseInt(st.nextToken());
            }
        }
        init();
        for (int i = 0; i < shapes.size(); i++) {
            for (int j = 0 ; j < 4; j++) {
                getScore(shapes.get(i));
                getScore(reflect(shapes.get(i)));
                shapes.set(i, rotate(shapes.get(i)));
            }
        }
        System.out.println(Collections.max(scores));
    }

    public static void init() {
        int[][] basicShape1 = {
                {1, 1, 1, 1}
        };
        shapes.add(basicShape1);
        int[][] basicShape2 = {
                {1, 1},
                {1, 1}
        };
        shapes.add(basicShape2);
        int[][] basicShape3 = {
                {1, 0},
                {1, 0},
                {1, 1}
        };
        shapes.add(basicShape3);
        int[][] basicShape4 = {
                {1, 0},
                {1, 1},
                {0, 1}
        };
        shapes.add(basicShape4);
        int[][] basicShape5 = {
                {1, 1, 1},
                {0, 1, 0}
        };
        shapes.add(basicShape5);
    }

    public static int[][] rotate(int[][] shape) {
        int R = shape.length;
        int C = shape[0].length;
        int[][] rotated = new int[C][R];
        for (int i = 0; i < C; i++) {
            for (int j = 0; j < R; j++) {
                rotated[i][j] = shape[R-1-j][i];
            }
        }
        return rotated;
    }

    public static int[][] reflect(int[][] shape) {
        int R = shape.length;
        int C = shape[0].length;
        int[][] reflected = new int[R][C];

        for (int i = 0; i < shape.length; i++) {
            for (int j = 0; j < shape[0].length; j++) {
                reflected[i][j] = shape[i][C - 1 - j];
            }
        }
        return reflected;
    }

    public static void getScore(int[][] shape) {
        for (int i = 0; i <= N - shape.length; i++) {
            for (int j = 0; j <= M - shape[0].length; j++) {
                scores.add(sum(i, j, shape));
            }
        }
    }

    public static int sum(int r, int c, int[][] shape) {
        int score = 0;
        for (int i = 0; i < shape.length; i++) {
            for (int j = 0; j < shape[0].length; j++) {
                if (shape[i][j] == 1) {
                    score += board[r + i][c + j];
                }
            }
        }
        return score;
    }
}
