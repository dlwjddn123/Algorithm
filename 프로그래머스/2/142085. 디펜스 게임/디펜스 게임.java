import java.util.*;

class Solution {
    public int solution(int n, int k, int[] enemy) {
        int answer = 0;
        PriorityQueue<Integer> pq = new PriorityQueue<>();
        
        for (int i = 0; i < enemy.length; i++) {
            n -= enemy[i];
            pq.add(-enemy[i]);
            if (n < 0 && k > 0) {
                n -= pq.poll();
                k -= 1;
            }else if (n < 0) {
                break;
            }
            answer += 1;
        }
        return answer;
    }
}