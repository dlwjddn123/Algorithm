import java.util.*;

class Solution {
    public int solution(String s) {
        int answer = s.length();
        // String a = "";
        for (int i = 1; i < s.length() / 2 + 1; i++) {
            String compacted = compact(s, i);
            
            if (compacted.length() < answer) {
                answer = compacted.length();
                // a = compacted;
            }
        }
        // System.out.println(a);
        return answer;
    }
    
    public String compact(String s, int unit) {
        StringBuilder sb = new StringBuilder();
        String current = s.substring(0, unit);
        int count = 1;
        
        for (int i = unit; i < s.length(); i += unit) {
            if (i + unit <= s.length()) {
                String next = s.substring(i, i + unit);
                if (current.equals(next)) {
                    count += 1;
                    continue;
                }
                if (count > 1) {
                    sb.append(count + current);
                    count = 1;
                    current = next;
                    continue;
                }
                sb.append(current);
                current = next;
                continue;
            }
        }
        
        if (count > 1) {
            sb.append(count + current);
            sb.append(s.substring(s.length() - s.length() % unit));
        }
        else {
            sb.append(s.substring(s.length() - s.length() % unit - unit));
        }
        
        return sb.toString();
    }
}