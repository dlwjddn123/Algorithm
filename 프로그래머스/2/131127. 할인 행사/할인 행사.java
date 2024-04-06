import java.util.*;

class Solution {
    public int solution(String[] want, int[] number, String[] discount) {
        int answer = 0;
        int total = Arrays.stream(number).sum();
        int p1 = 0;
        int p2 = 0;
        Map<String, Integer> products = new HashMap<>();
        
        for (int i = 0; i < want.length; i++) {
            products.put(want[i], number[i]);
        }
        
        while (p1 <= p2 && p2 < discount.length) {
            if (p2 - p1 > 9) {
                if (products.get(discount[p1]) != null) {
                    if (products.get(discount[p1]) >= 0) {
                        total += 1;
                    }
                    products.put(discount[p1], products.get(discount[p1]) + 1);
                }
                p1 += 1;
                continue;
            }
            if (products.get(discount[p2]) != null) {
                if (products.get(discount[p2]) > 0) {
                    total -= 1;
                }
                products.put(discount[p2], products.get(discount[p2]) - 1);
            }
            p2 += 1;
            
            if (total == 0) {
                answer += 1;
            }
        }
        return answer;
    }
}