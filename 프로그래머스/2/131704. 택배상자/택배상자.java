import java.util.*;

class Solution {
    public int solution(int[] order) {
        int answer = 0;
        Queue<Integer> belt = new LinkedList<>();
        Stack<Integer> sub = new Stack<>();
        
        for (int i = 1; i < order.length + 1; i++) {
            belt.add(i);
        }
        
        for (int number : order) {
            if ((belt.isEmpty() || belt.peek() > number) && !sub.isEmpty() && sub.peek() != number) {
                return answer;
            }
            if (!belt.isEmpty() && belt.peek() <= number) {
                int size = belt.size();
                for (int i = 0; i < size; i++) {
                    if (number > belt.peek()) {
                        sub.push(belt.poll());
                        continue;
                    }
                    if (number == belt.peek()) {
                        answer += 1;
                        belt.poll();
                        break;
                    }
                }    
            }
            if (!sub.isEmpty() && sub.peek() == number) {
                while (!sub.isEmpty()) {
                    if (sub.peek() != number) {
                        break;
                    } 
                    answer += 1;
                    sub.pop();                      
                }                
            }
        }
        return answer;
    }
}