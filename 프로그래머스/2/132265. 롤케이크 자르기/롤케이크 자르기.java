import java.util.*;

class Solution {
    public int solution(int[] topping) {
        int answer = 0;
        int[] front = new int[topping.length];
        int[] back = new int[topping.length];
        Set<Integer> fset = new HashSet<>();
        Set<Integer> bset = new HashSet<>();
        
        for (int i = 0; i < topping.length; i++) {
            fset.add(topping[i]);
            front[i] = fset.size();
        }
        
        for (int j = topping.length - 1; j >= 0; j--) {
            bset.add(topping[j]);
            back[j] = bset.size();
        }
        
        for (int i = 0; i < topping.length - 1; i++) {
            if (front[i] == back[i + 1]) {
                answer += 1;
            }
        }
        
        return answer;
    }
}