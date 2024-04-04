import java.util.*;


class Solution {
    public static int[] dx = {0, 0, -1, 1};
    public static int[] dy = {-1, 1, 0, 0};
    
    public int solution(int[][] maps) {
        int answer = findMinDistanceToTheEnemyCamp(maps);
        return answer;
    }
    
    public int findMinDistanceToTheEnemyCamp(int[][] maps) {
        boolean[][] visited = new boolean[maps.length][maps[0].length];
        visited[0][0] = true;
        Queue<int[]> queue = new ArrayDeque<>();
        queue.add(new int[]{0, 0, 1});
        
        while (!queue.isEmpty()) {
            int[] current = queue.poll();
            
            for (int i = 0; i < 4; i++) {
                int nx = dx[i] + current[0];
                int ny = dy[i] + current[1];
                if (ny == maps.length - 1 && nx == maps[0].length) {
                    return current[2];
                }
                if (0 <= nx && nx < maps[0].length && 0 <= ny && ny < maps.length && !visited[ny][nx]) {
                    visited[ny][nx] = true;
                    if (maps[ny][nx] == 1) {
                        queue.add(new int[]{nx, ny, current[2] + 1});
                    }
                }
            }
        }
        return -1;
    }
}