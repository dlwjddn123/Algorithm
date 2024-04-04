import java.util.*;

class Solution {
    public int solution(int[] arrayA, int[] arrayB) {
        List<Integer> numbers = new ArrayList<>();
        
        Arrays.sort(arrayA);
        Arrays.sort(arrayB);
        
        numbers.add(findNumber(arrayA, arrayB));
        numbers.add(findNumber(arrayB, arrayA));
        
        return Collections.max(numbers);
    }
    
    public int findNumber(int[] arr, int[] target) {
        int minNumber = arr[0];
        if (minNumber < 2) {
            return 0;
        }
        List<Integer> result = new ArrayList<>();
        List<Integer> cases = getCases(minNumber);
        cases.sort(Comparator.reverseOrder());
        
        for (int num : cases) {
            boolean isPossible = true;
            for (int i = 0; i < arr.length; i++) {
                if (arr[i] % num != 0 || target[i] % num == 0) {
                    isPossible = false;
                    break;
                }
            }    
            if (isPossible) {
                return num;
            }
        }
        
        return 0;
    }
    
    public List<Integer> getCases(int minNumber) {
        List<Integer> cases = new ArrayList<>();
        
        for (int i = 2; i <= minNumber; i++) {
            if (minNumber % i == 0) {
                cases.add(i);
            }
        }
        return cases;
    }
}

