import java.util.*;
import java.io.*;

class Solution {
    public int solution(int[] elements) {
        int N = elements.length;
        Set<Integer> result = new HashSet<>();
        
        for (int i = 0; i < N; i++) {
            int total = 0;
            for (int j = 0; j < N; j++) {
                total += elements[(i + j) % N];
                result.add(total);
            }
        }
        
        return result.size();
    }
}