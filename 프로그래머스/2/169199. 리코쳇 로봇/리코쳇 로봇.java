import java.util.*;

class Solution {    
    public static int[] dx = {0, 0, -1, 1};
    public static int[] dy = {-1, 1, 0, 0};
    public static String[][] myBoard;
    public static Point start;
    public static Point target;
    
    public class Point {
        int x;
        int y;
        int dist;
        public Point(int x, int y, int dist) {
            this.x = x;
            this.y = y;
            this.dist = dist;
        }
    }

    public int solution(String[] board) {
        int answer = -1;
        
        setup(board);
        
        answer = bfs();
        
        return answer;
    }

    public void setup(String[] input) {
        myBoard = new String[input.length][input[0].length()];

        for (int i = 0; i < myBoard.length; i++) {
            myBoard[i] = input[i].split("");
        }
        setStartAndTargetPoint(myBoard);
    }

    public void setStartAndTargetPoint(String[][] board) {
        for (int i = 0; i < board.length; i++) {
            for (int j = 0; j < board[0].length; j++) {
                if (board[i][j].equals("R")) {
                    start = new Point(j, i, 0);
                } else if (board[i][j].equals("G")) {
                    target = new Point(j, i, 0);
                }
                if (start != null && target != null) {
                    break;
                }
            }
        }
    }
    
    public int bfs() {
        boolean[][] visited = new boolean[myBoard.length][myBoard[0].length];
        visited[start.y][start.x] = true;
        
        Queue<Point> queue = new LinkedList<>();
        queue.add(start);
        
        while (!queue.isEmpty()) {
            Point current = queue.poll();
            
            for (int i = 0; i < 4; i++) {
                int ny = current.y + dy[i];
                int nx = current.x + dx[i];
                if (0 <= nx && nx < myBoard[0].length && 0 <= ny && ny < myBoard.length && !myBoard[ny][nx].equals("D")) {
                    Point movedCurrent = move(current, i, visited);    
                    if (!visited[movedCurrent.y][movedCurrent.x]) {
                        if (myBoard[movedCurrent.y][movedCurrent.x].equals("G")) {
                            return movedCurrent.dist;
                        }
                        visited[movedCurrent.y][movedCurrent.x] = true;
                        queue.add(movedCurrent);
                    }
                }
            }
        }
        return -1;
    }
    
    public Point move(Point point, int direct, boolean[][] visited) {
        Point current = new Point(point.x, point.y, point.dist + 1);
        while (true) {
            int nx = current.x + dx[direct];
            int ny = current.y + dy[direct];
            
            if (0 <= nx && nx < myBoard[0].length && 0 <= ny && ny < myBoard.length) {
                if (myBoard[ny][nx].equals("D")) {
                    break;
                }
                current.x += dx[direct];
                current.y += dy[direct];
                continue;
            }
            break;
        }
        return current;
    }

}