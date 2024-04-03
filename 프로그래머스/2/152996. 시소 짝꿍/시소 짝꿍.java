import java.util.*;

class Solution {
    public long solution(int[] weights) {
        long answer = 0;
        boolean[] visited = new boolean[1001];
        int[] counts = new int[1001];
        int[][] c = new int[][]{{2, 2}, {2, 3}, {2, 4}, {3, 2}, {3, 4}, {4, 2}, {4, 3}};
        Map<Integer, Integer> map = new HashMap<>();
        Arrays.sort(weights);
        
        for (int i = 0 ; i < weights.length; i++) {
            if (map.get(weights[i]) == null) {
                map.put(weights[i], 1);
                continue;
            }
            map.put(weights[i], map.get(weights[i]) + 1);
        }
        
        for (int i = 0; i < weights.length - 1; i++) {
            if (!visited[weights[i]]) {
                visited[weights[i]] = true;
                int count = 0;
                for (int j = i + 1; j < weights.length; j++) {
                    if (weights[i] == weights[j]) {
                        continue;
                    }
                    for (int k = 0; k < c.length; k++) {
                        if (weights[i] * c[k][0] == weights[j] * c[k][1]) {
                            count += 1;
                            break;
                        }
                    }
                }
                counts[weights[i]] = count;
            }
            answer += counts[weights[i]] + (map.get(weights[i]) - 1);
            map.put(weights[i], map.get(weights[i]) - 1);

        }
        
        return answer;
    }
}