import java.util.*;

class Solution {
    public int solution(String[][] board, int h, int w) {
        int answer = 0;
        int row = board.length;
        int col = board[0].length;
        int[] dx = {0, 0, -1, 1};
        int[] dy = {-1, 1, 0, 0};
        
        for (int i = 0; i < 4; i++) {
            int nx = dx[i] + w;
            int ny = dy[i] + h;
            if (0 <= nx && nx < col && 0 <= ny && ny < row && board[ny][nx].equals(board[h][w])){
                answer += 1;
            }
        }
        
        return answer;
    }
}