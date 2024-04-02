import java.util.*;


class Solution {
    public int solution(int[] queue1, int[] queue2) {
        int count = 0;
        Queue<Long> q1 = new LinkedList<>();
        Queue<Long> q2 = new LinkedList<>();
        long q1Sum = 0;
        long q2Sum = 0;
        
        for (int i = 0; i < queue1.length; i++) {
            q1.add((long) queue1[i]);
            q1Sum += queue1[i];
        }
        
        for (int i = 0; i < queue2.length; i++) {
            q2.add((long) queue2[i]);
            q2Sum += queue2[i];
        }
        
        while (count < (queue1.length + queue2.length) * 2 + 2) {
            if (q1Sum == q2Sum) {
                return count;
            }
            
            if (q1Sum > q2Sum) {
                long temp = q1.poll();
                q2.add(temp);
                q1Sum -= temp;
                q2Sum += temp;
            } else if (q2Sum > q1Sum) {
                long temp = q2.poll();
                q1.add(temp);
                q2Sum -= temp;
                q1Sum += temp;    
            }
            count += 1;
        }
        
        return -1;
    }
}