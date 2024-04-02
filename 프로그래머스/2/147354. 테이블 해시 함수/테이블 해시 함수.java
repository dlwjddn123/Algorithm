import java.util.*;

class Solution {
    public int solution(int[][] data, int col, int row_begin, int row_end) {
        int answer = 0;
    
        Arrays.sort(data, (o1, o2) -> {
            if (o1[col-1] != o2[col-1]) {
                return Integer.compare(o1[col-1], o2[col-1]);
            }
            return Integer.compare(o2[0], o1[0]);
        });
        
        for (int i = row_begin-1; i < row_end; i++) {
            int total = 0;
            for (int j = 0; j < data[i].length; j++) {
                total += data[i][j] % (i+1);
            }
            if (i == row_begin-1) {
                answer = total;
                continue;
            }
            answer ^= total;
        }
        
        
        return answer;
    }
}