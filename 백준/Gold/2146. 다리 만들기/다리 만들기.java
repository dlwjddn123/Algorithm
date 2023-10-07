import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {

    private static int islandCount = 0;
    private static int N;
    private static int DIRECT = 4;
    private static List<Integer> visitedIsland = new ArrayList<>();
    private static List<Integer> bridges = new ArrayList<>();
    private static int[][] board;
    private static int[] dx = {0, 0, -1, 1};
    private static int[] dy = {-1, 1, 0, 0};

    static class Point {
        private int x, y, dist;

        public Point(int x, int y, int dist) {
            this.x = x;
            this.y = y;
            this.dist = dist;
        }

        public Point(int x, int y) {
            this.x = x;
            this.y = y;
        }

        public int getX() {
            return x;
        }

        public int getY() {
            return y;
        }

        public int getDist() {
            return dist;
        }
    }

    public static void main(String[] args) throws IOException {
        input();
        findIsland();
        for (int row = 0; row < N; row++) {
            for (int col = 0; col < N; col++) {
                if (board[row][col] != 0 && !visitedIsland.contains(board[row][col])) {
                    findShortestBridge(new Point(col, row, 0));
                }
            }
        }
        System.out.println(Collections.min(bridges));
    }

    public static void input() throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        N = Integer.parseInt(br.readLine());
        board = new int[N][N];
        for (int row = 0; row < N; row++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            for (int col = 0; col < N; col++) {
                board[row][col] = Integer.parseInt(st.nextToken());
            }
        }
    }

    public static void findIsland() {
        boolean[][] visited = new boolean[N][N];
        for (int row = 0; row < N; row++) {
            for (int col = 0; col < N; col++) {
                if (!visited[row][col] && board[row][col] == 1) {
                    find(visited, new Point(col, row));
                }
            }
        }
    }

    private static void find(boolean[][] visited, Point startPoint) {
        islandCount += 1;
        Queue<Point> queue = new LinkedList<>();
        queue.add(startPoint);
        visited[startPoint.getY()][startPoint.getX()] = true;
        board[startPoint.getY()][startPoint.getX()] = islandCount;
        while (!queue.isEmpty()) {
            int nx, ny;
            Point point = queue.poll();
            for (int idx = 0; idx < DIRECT; idx++) {
                nx = point.getX() + dx[idx];
                ny = point.getY() + dy[idx];
                if (0 <= nx && nx < N && 0 <= ny && ny < N && board[ny][nx] == 1 &&!visited[ny][nx]) {
                    visited[ny][nx] = true;
                    board[ny][nx] = islandCount;
                    queue.add(new Point(nx, ny));
                }
            }
        }
    }

    public static void findShortestBridge(Point startPoint) {
        int islandNumber = board[startPoint.getY()][startPoint.getX()];
        visitedIsland.add(islandNumber);
        boolean[][] visited = new boolean[N][N];
        Deque<Point> queue = new ArrayDeque<>();
        queue.add(startPoint);
        while (!queue.isEmpty()) {
            int nx, ny;
            Point point = queue.poll();
            for (int idx = 0; idx < DIRECT; idx++) {
                nx = point.getX() + dx[idx];
                ny = point.getY() + dy[idx];
                if (0 <= nx && nx < N && 0 <= ny && ny < N && !visited[ny][nx]) {
                    if (board[ny][nx] == islandNumber) {
                        visited[ny][nx] = true;
                        queue.addFirst(new Point(nx, ny, point.getDist()));
                        continue;
                    }
                    if (board[ny][nx] != 0) {
                        bridges.add(point.getDist());
                        return;
                    }
                    visited[ny][nx] = true;
                    queue.add(new Point(nx, ny, point.getDist() + 1));
                }
            }
        }
    }
}
