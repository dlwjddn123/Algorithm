import java.util.*;

class Solution {
    public int solution(int[] cards) {
        int answer = 0;
        for (int i = 0; i < cards.length; i++) {
            Map<Integer, Boolean> group1 = findGroup(cards, i);
            int max = 0;
            
            for (int j = 0; j < cards.length; j++) {
                if (group1.containsKey(j)) {
                    continue;
                }
                
                int groupSize = findGroup(cards, j).size();
                max = (groupSize > max) ? groupSize : max;
            }
            
            answer = (group1.size() * max > answer) ? group1.size() * max : answer;
        }
        return answer;
    }
    
    public Map<Integer, Boolean> findGroup(int[] cards, int N) {
        Map<Integer, Boolean> group = new HashMap<>();
        boolean isNotChecked = true;
        int next = N;    
        
        while (isNotChecked) {
            if (group.containsKey(next)) {
                break;   
            }
            group.put(next, true);
            next = cards[next] - 1;
        }
        
        return group;
    }
}