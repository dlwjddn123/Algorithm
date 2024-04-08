import java.util.*;


class Solution {
    public int solution(int n, int[][] wires) {
        int answer = n;
        Map<Integer, List<Integer>> wireMap = new HashMap<>();
        
        for (int[] wire : wires) {
            if (wireMap.get(wire[0]) == null) {
                wireMap.put(wire[0], new ArrayList<>());
            }
            wireMap.get(wire[0]).add(wire[1]);
            if (wireMap.get(wire[1]) == null) {
                wireMap.put(wire[1], new ArrayList<>());
            }
            wireMap.get(wire[1]).add(wire[0]);
        }
        
        for (int[] wire : wires) {
            cutWire(wireMap, wire);
            int count = findDiffTopCount(wireMap, n);
            if (count < answer) {
                answer = count;
            }
            restoreWire(wireMap, wire);
        }
        
        return answer;
    }
    
    public void restoreWire(Map<Integer, List<Integer>> wireMap, int[] wire) {
        wireMap.get(wire[0]).add(Integer.valueOf(wire[1]));
        wireMap.get(wire[1]).add(Integer.valueOf(wire[0]));
    }
    
    public void cutWire(Map<Integer, List<Integer>> wireMap, int[] wire) {
        wireMap.get(wire[0]).remove(Integer.valueOf(wire[1]));
        wireMap.get(wire[1]).remove(Integer.valueOf(wire[0]));
    }
    
    public int findDiffTopCount(Map<Integer, List<Integer>> wireMap, int totalTopCount) {
        boolean[] visited = new boolean[totalTopCount + 1];
        List<Integer> result = new ArrayList<>();
        
        for (int topNumber : wireMap.keySet()) {
            if (!visited[topNumber]) {
                result.add(getTopCount(wireMap, visited, topNumber));
            }
        }
        
        return Math.abs(result.get(0) - result.get(1));
    }
    
    public int getTopCount(Map<Integer, List<Integer>> wireMap, boolean[] visited, int topNumber) {
        int count = 1;
        Queue<Integer> queue = new ArrayDeque<>();
        visited[topNumber] = true;
        queue.add(topNumber);
        
        while (!queue.isEmpty()) {
            int topNum = queue.poll();
            for (Integer nextTopNum : wireMap.get(topNum)) {
                if (!visited[nextTopNum]) {
                    visited[nextTopNum] = true;
                    count += 1;
                    queue.add(nextTopNum);
                }
            }
        }
        
        return count;
    }
    
}