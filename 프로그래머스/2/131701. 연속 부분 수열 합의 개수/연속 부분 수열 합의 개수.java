import java.util.*;


class Solution {
    public int solution(int[] elements) {
        Set<Integer> result = new HashSet<>();
        List<Integer> numbers = new LinkedList<>();
        
        for (int i = 0; i < elements.length; i++) {
            numbers.add(elements[i]);
        }
        
        for (int j = 0; j < elements.length + 1; j++) {
            numbers.add(numbers.get(0));
            numbers.remove(0);
            int sum = 0;
            for (Integer number : numbers) {
                sum += number;
                result.add(sum);
            }
        }
        
        return result.size();
    }
}