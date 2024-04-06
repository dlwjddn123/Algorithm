import java.util.*;

class Solution {
    public int solution(int[] scoville, int K) {
        int answer = 0;
        PriorityQueue<Integer> pq = new PriorityQueue<>();
        for (int i = 0; i < scoville.length; i++) {
            pq.add(scoville[i]);
        }
        
        while (!pq.isEmpty()) {
            int first = pq.poll();
            if (pq.isEmpty()) {
                if (first < K) {
                    answer = -1;
                }
                break;
            }
            
            if (first >= K) {
                break;
            }
            
            int second = pq.poll();
            pq.add(first + second * 2);
            answer += 1;
        }
        
        return answer;
    }
}