import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    public static int N, M;
    public static char[][] board;
    public static int[] dx = {0, 0, -1, 1};
    public static int[] dy = {-1, 1, 0, 0};
    public static int rx, ry, bx, by, ox, oy;
    public static boolean isGoal, isFail;

    static class Points {
        int rx, ry, bx, by;
        public Points(int rx, int ry, int bx, int by) {
            this.rx = rx;
            this.ry = ry;
            this.bx = bx;
            this.by = by;
        }
    }

    public static void main(String[] args) throws IOException {
        setup();
        if (bfs(rx, ry, bx, by)) {
            System.out.println(1);
        } else {
            System.out.println(0);
        }
    }

    public static void setup() throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());
        board = new char[N][M];

        for (int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine());
            String input = st.nextToken();
            for (int j = 0; j < M; j++) {
                char c = input.charAt(j);
                if (c == 'O') {
                    ox = j;
                    oy = i;
                }
                if (c == 'R') {
                    rx = j;
                    ry = i;
                }
                if (c == 'B') {
                    bx = j;
                    by = i;
                }
                board[i][j] = c;
            }
        }
    }

    public static boolean bfs(int rx, int ry, int bx, int by) {
        Queue<List<Points>> outQueue = new LinkedList<>();
        Queue<Points> inQueue = new LinkedList<>();

        outQueue.add(List.of(new Points(rx, ry, bx, by)));
        int count = 0;

        while (!outQueue.isEmpty() && count < 10) {
            count += 1;

            List<Points> points = outQueue.poll();
            for (Points p : points) {
                inQueue.add(p);
            }
            List<Points> nextQueueStorage = new ArrayList<>();
            while (!inQueue.isEmpty()) {
                Points p = inQueue.poll();

                for (int i = 0; i < 4; i++) {
                    isFail = false;
                    isGoal = false;
                    Points nextPoint = move(p, dx[i], dy[i]);
                    if (nextPoint == null) {
                        continue;
                    }
                    if (isGoal && !isFail) {
                        return true;
                    }
                    nextQueueStorage.add(nextPoint);
                }
            }

            if (!nextQueueStorage.isEmpty()) {
                outQueue.add(nextQueueStorage);
            }
        }

        return false;
    }

    public static Points move(Points current, int dx, int dy) {
        int n = 0;
        int rx = current.rx;
        int ry = current.ry;
        int bx = current.bx;
        int by = current.by;
        boolean flag = false;

        if (dy == -1 || dy == 1) {
            n = N;
        } else if (dx == -1 || dx == 1) {
            n = M;
        }

        for (int i = 0; i < n; i++) {
            rx += dx;
            ry += dy;
            if (0 <= rx && rx <= M-1 && 0 <= ry && ry <= N-1) {
                if (rx == ox && ry == oy) {
                    isGoal = true;
                    rx = -1;
                    ry = -1;
                    break;
                } else if (board[ry][rx] == '#') {
                    rx -= dx;
                    ry -= dy;
                    break;
                } else if (bx == rx && by == ry) {
                    flag = true;
                    break;
                }
            }
        }
        for (int i = 0; i < n; i++) {
            bx += dx;
            by += dy;
            if (0 <= bx && bx <= M-1 && 0 <= by && by <= N-1) {
                if (bx == ox && by == oy) {
                    isFail = true;
                    return null;
                } else if (board[by][bx] == '#' || (bx == rx && by == ry)) {
                    bx -= dx;
                    by -= dy;
                    break;
                }
            }
        }
        if (flag) {
            rx = bx - dx;
            ry = by - dy;
        }
        return new Points(rx, ry, bx, by);
    }
}
