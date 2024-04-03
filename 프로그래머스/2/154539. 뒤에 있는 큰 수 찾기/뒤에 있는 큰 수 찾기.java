import java.util.*;

class Solution {
    class Number implements Comparable<Number> {
        int value;
        int idx;
        
        Number(int value, int idx) {
            this.value = value;
            this.idx = idx;
        }
        
        int getValue() {
            return this.value;
        }
        
        int getIdx() {
            return this.idx;
        }
        
        @Override
        public int compareTo(Number number) {
            return this.value - number.getValue();
        }
    }
    
    public int[] solution(int[] numbers) {
        int[] answer = new int[numbers.length];
        PriorityQueue<Number> pq = new PriorityQueue<>();
        
        for (int i = 0; i < numbers.length; i++) {
            if (i < numbers.length - 1 && numbers[i] < numbers[i + 1]) {
                answer[i] = numbers[i + 1];
            }
            
            while (!pq.isEmpty() && pq.peek().getValue() < numbers[i]) {
                Number number = pq.poll();
                answer[number.getIdx()] = numbers[i];
                
            }
            
            pq.add(new Number(numbers[i], i));
            
        }
        
        for (int i = 0; i < answer.length; i++) {
            if (answer[i] == 0) {
                answer[i] = -1;
            }
        }
        
        return answer;
    }
}