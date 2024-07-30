import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Deque;
import java.util.LinkedList;
import java.util.StringTokenizer;

public class Main {

    public static String[][] board;
    public static int N, M;
    public static int[] dx = {0, 0, -1, 1};
    public static int[] dy = {-1, 1, 0, 0};

    static class Point {
        int x, y, dist;
        public Point(int x, int y, int dist) {
            this.x = x;
            this.y = y;
            this.dist = dist;
        }

        @Override
        public String toString() {
            return "x = " + x + " y = " + y + " dist = " + dist;
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        M = Integer.parseInt(st.nextToken());
        N = Integer.parseInt(st.nextToken());

        if (N == 1 && M == 1) {
            System.out.println(0);
            return;
        }
        
        board = new String[N][M];

        for (int i = 0; i < N; i++) {
            board[i] = br.readLine().split("");
        }

        Deque<Point> queue = new LinkedList<>();
        queue.add(new Point(0, 0, 0));
        boolean[][] visited = new boolean[N][M];

        while (!queue.isEmpty()) {
            Point current = queue.poll();
            for (int i = 0; i < 4; i++) {
                int nx = current.x + dx[i];
                int ny = current.y + dy[i];
                if (nx == M-1 && ny == N-1) {
                    System.out.println(current.dist);
                    return;
                }
                if (0 <= nx && nx < M && 0 <= ny && ny < N && !visited[ny][nx]) {
                    visited[ny][nx] = true;
                    if (board[ny][nx].equals("0")) {
                        queue.addFirst(new Point(nx, ny, current.dist));
                        continue;
                    }
                    queue.add(new Point(nx, ny, current.dist + 1));
                }
            }
        }
    }
}
