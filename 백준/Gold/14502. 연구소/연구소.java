import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    private static final int EMPTY = 0;
    private static final int WALL = 1;
    private static final int VIRUS = 2;
    private static final int MAX_CASE_SIZE = 3;
    private static final int[] dx = {0, 0, 1, -1};
    private static final int[] dy = {-1, 1, 0, 0};

    private static int N;
    private static int M;
    private static List<Point> emptyPoints = new ArrayList<>();
    private static List<WallPoints> allWallPoints = new ArrayList<>();
    private static List<Point> virusPoints = new ArrayList<>();
    private static int[][] area;
    private static List<Integer> result = new ArrayList<>();

    public static void main(String[] args) throws IOException {
        System.out.println(solution());
    }
    public static class Point {
        private int x;
        private int y;

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
    }

    public static class WallPoints {
        private List<Point> points;

        public WallPoints(List<Point> points) {
            this.points = points;
        }

        public List<Point> getPoints() {
            return points;
        }
    }

    public static void findAllWallPoints(List<Point> points, int curIndex) {
        if (points.size() == MAX_CASE_SIZE) {
            allWallPoints.add(new WallPoints(new ArrayList<>(points)));
            return;
        }

        for (int i = curIndex; i < emptyPoints.size(); i++) {
            points.add(emptyPoints.get(i));
            findAllWallPoints(points, i + 1);
            points.remove(points.size() - 1);
        }
    }

    public static void setEmptyPointsAndVirusPoints() {
        for (int row = 0; row < N; row++) {
            for (int col = 0; col < M; col++) {
                if (area[row][col] == EMPTY) {
                    emptyPoints.add(new Point(col, row));
                    continue;
                }
                if (area[row][col] == VIRUS) {
                    virusPoints.add(new Point(col, row));
                }
            }
        }
    }

    public static void findSafetyArea(WallPoints wallPoints) {
        makeWall(wallPoints);
        int virusAreaCount = virusDiffusion();
        int safetyAreaCount = 0;

        for (int row = 0; row < N; row++) {
            for (int col = 0; col < M; col++) {
                if (area[row][col] == EMPTY) {
                    safetyAreaCount += 1;
                }
            }
        }
        result.add(safetyAreaCount - virusAreaCount);
        removeWall(wallPoints);
    }

    public static void removeWall(WallPoints wallPoints) {
        for (Point point : wallPoints.getPoints()) {
            area[point.getY()][point.getX()] = EMPTY;
        }
    }

    public static int  virusDiffusion() {
        boolean[][] visited = new boolean[N][M];
        Queue<Point> queue = new LinkedList<>();
        setStartPoints(queue);
        int virusAreaCount = 0;

        while (!queue.isEmpty()) {
            Point point = queue.poll();
            for (int i = 0; i < 4; i++) {
                int nx = dx[i] + point.getX();
                int ny = dy[i] + point.getY();
                if (0 <= nx && nx < M && 0 <= ny && ny < N && !visited[ny][nx] && area[ny][nx] == EMPTY) {
                    visited[ny][nx] = true;
                    queue.add(new Point(nx, ny));
                    virusAreaCount += 1;
                }
            }
        }
        return virusAreaCount;
    }

    public static void setStartPoints(Queue<Point> queue) {
        for (Point point : virusPoints) {
            queue.add(point);
        }
    }

    public static void makeWall(WallPoints wallPoints) {
        for (Point point : wallPoints.getPoints()) {
            area[point.getY()][point.getX()] = WALL;
        }
    }

    public static int solution() throws IOException {
        processInputData();
        setEmptyPointsAndVirusPoints();
        findAllWallPoints(new ArrayList<>(), 0);
        for (WallPoints wallPoints : allWallPoints) {
            findSafetyArea(wallPoints);
        }
        return Collections.max(result);
    }

    public static void processInputData() throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());
        area = new int[N][M];

        for (int row = 0; row < N; row++) {
            st = new StringTokenizer(br.readLine());
            for (int col = 0; col < M; col++) {
                area[row][col] = Integer.parseInt(st.nextToken());
            }
        }
    }

}
