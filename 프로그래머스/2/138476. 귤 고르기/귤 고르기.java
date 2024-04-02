import java.util.*;

class Solution {
    public int solution(int k, int[] tangerine) {
        int answer = 0;
        Integer[] map = new Integer[10000001];
        Arrays.fill(map, 0);
        
        for (int t : tangerine) {
            map[t] += 1;
        }
        Arrays.sort(map, Collections.reverseOrder());
        
        for (int i = 0; i < map.length; i++) {
            k -= map[i];
            
            if (k <= 0) {
                answer = i + 1;
                break;
            }
        }
        
        return answer;
    }
}