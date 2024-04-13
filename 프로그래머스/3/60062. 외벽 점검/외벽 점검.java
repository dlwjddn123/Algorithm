import java.util.*;

class Solution {
    public static List<List<Integer>> weakCase = new ArrayList<>();
    public static List<List<Integer>> distCase = new ArrayList<>();
    
    public int solution(int n, int[] weak, int[] dist) {
        int answer = dist.length + 1;
        List<Integer> dists = new LinkedList<>();
        List<Integer> weaks = new ArrayList<>();
        List<Integer> result = new ArrayList<>();
        
        for (int d : dist) {
            dists.add(d);
        }
        
        for (int w : weak) {
            weaks.add(w);
        }
        
        findWeakCase(weaks, n);
        findDistCase(new boolean[dist.length], new ArrayList<>(), dists);
        
        for (List<Integer> wcase : weakCase) {
            for (List<Integer> dcase : distCase) {
                int cur = 0, next;
                int dist_idx = 0;
                while(cur < wcase.size() && dist_idx < dcase.size()){
                    next = cur+1;
                    while(next < wcase.size() &&
                            wcase.get(cur) + dcase.get(dist_idx) >= wcase.get(next)){
                       next++;
                    }
                    cur = next;
                    dist_idx++;
                }

                if(cur == wcase.size() && dist_idx < answer) {
                    answer = dist_idx;
                }
            }
        }
        
        if (answer == dist.length + 1) {
            return -1;
        }
        return answer;
    }
    
    public void findWeakCase(List<Integer> weak, int n) {
        weakCase.add(new ArrayList<>(weak));
        for (int i = 0; i < weak.size() - 1; i++) {
            weak.add(weak.get(0) + n);
            weak.remove(0);
            weakCase.add(new ArrayList<>(weak));
        }
    }
    
    public void findDistCase(boolean[] visited, List<Integer> current, List<Integer> dist) {
        if (current.size() == dist.size()) {
            distCase.add(new ArrayList<>(current));
            return;
        }
        
        for (int i = 0; i < dist.size(); i++) {
            if (!visited[i]) {
                visited[i] = true;
                current.add(dist.get(i));
                findDistCase(visited, current, dist);
                current.remove(current.size() - 1);        
                visited[i] = false;
            }
        }
    }
}