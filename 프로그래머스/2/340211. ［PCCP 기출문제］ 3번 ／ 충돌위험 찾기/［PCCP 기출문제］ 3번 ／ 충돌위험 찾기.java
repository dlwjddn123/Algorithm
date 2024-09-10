import java.util.*;

class Solution {
    
    static int R;
    static int C; 
    static Map<Integer, Point> pointMap = new HashMap<>();
    static final int[] dx = {0, 0, -1, 1};
    static final int[] dy = {-1, 1, 0, 0};
    
    class Point {
        int x, y;
        Point parent;
        public Point(int x, int y) {
            this.x = x;
            this.y = y;
            this.parent = null;
        }
        
        @Override
        public boolean equals(Object obj) {
            if (this == obj) return true;
            if (obj == null || getClass() != obj.getClass()) return false;
            Point point = (Point) obj;
            return x == point.x && y == point.y;
        }

        @Override
        public int hashCode() {
            return Objects.hash(x, y);
        }
    }
    
    public int solution(int[][] points, int[][] routes) {
        int answer = 0;
        setBoardSize(points);
        setPointMap(points);
        
        int longestRouteDist = 0;
        List<List<Point>> shortestRoutes = new ArrayList<>();
        for (int[] r : routes) {
            List<Point> route = findShortestRoute(r);
            shortestRoutes.add(route);     
            longestRouteDist = (longestRouteDist < route.size()) ? route.size() : longestRouteDist;
        }
        
        answer = findStrikeCount(shortestRoutes, longestRouteDist);
        
        return answer;
    }
    
    public void setBoardSize(int[][] points) {
        int r = 0;
        int c = 0;
        for (int[] point : points) {
            if (point[0] > r) {
                r = point[0];
            }
            if (point[1] > c) {
                c = point[1];
            }
        }
        R = r;
        C = c;
    }
    
    public void setPointMap(int[][] points) {
        for (int i = 0; i < points.length; i++) {
            pointMap.put(i + 1, new Point(points[i][1], points[i][0]));
        }
    }
    
    public int findStrikeCount(List<List<Point>> shortestRoutes, int longestRouteDist) {
        int totalCount = 0;
        
        for (int i = 0; i < longestRouteDist; i++) {
            Map<Point, Integer> countMap = new HashMap<>();
            
            for (List<Point> shortestRoute : shortestRoutes) {
                Point point = (shortestRoute.size() > i) ? shortestRoute.get(i) : null;
                if (point != null) {
                    if (countMap.get(point) == null) {
                        countMap.put(point, 1);
                        continue;
                    }
                    countMap.put(point, countMap.get(point) + 1);
                }
            }
            
            for (Integer count : countMap.values()) {
                if (count > 1) {
                    totalCount += 1;
                }
            }
        }
        
        return totalCount;
    }
    
    public List<Point> findShortestRoute(int[] routePoints) {
        List<Point> shortestRoute = new ArrayList<>();
        for (int i = 1; i < routePoints.length; i++) {
            Point start = pointMap.get(routePoints[i - 1]);
            Point end = pointMap.get(routePoints[i]);
            bfs(start, end, shortestRoute);
        }
        return shortestRoute;
    }
    
    public void bfs(Point start, Point end, List<Point> shortestRoute) {
        boolean[][] visited = new boolean[R + 1][C + 1];
        visited[start.y][start.x] = true;
        Queue<Point> queue = new LinkedList<>();
        queue.add(start);
        if (shortestRoute.size() == 0) {
            shortestRoute.add(start);
        }
        
        while(!queue.isEmpty()) {
            Point current = queue.poll();
            if (current.x == end.x && current.y == end.y) {
                shortestRoute.addAll(getRoute(current));
                break;
            }
            for (int i = 0; i < 4; i++) {
                int nx = current.x + dx[i];
                int ny = current.y + dy[i];

                if (0 < nx && nx <= C && 0 < ny && ny <= R && !visited[ny][nx]) {
                    visited[ny][nx] = true;
                    Point next = new Point(nx, ny);
                    next.parent = current;
                    queue.add(next);
                }            
            }            
        }
    }
    
    public List<Point> getRoute(Point point) {
        List<Point> route = new ArrayList<>();
        while (point.parent != null) {
            route.add(point);
            point = point.parent;
        }
        Collections.reverse(route);
        return route;
    }
    
}