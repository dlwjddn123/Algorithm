import java.util.*;

class Solution {
    public static int MAX_LENGTH = 5;
    public static int number = -1;
    public static String[] alpha = new String[]{"A", "E", "I", "O", "U"};
    
    public int solution(String word) {
        Map<String, Integer> dict = new HashMap<>();
        
        recordOrderAllWordsToDict(dict, new ArrayList<>());
        
        return dict.get(word);
    }
    
    public void recordOrderAllWordsToDict(Map<String, Integer> dict, List<String> word) {
        number += 1;
        dict.put(String.join("", word), number);
        
        if (word.size() == MAX_LENGTH) {
            return;
        }
        
        for (int i = 0; i < MAX_LENGTH; i++) {
            word.add(alpha[i]);
            recordOrderAllWordsToDict(dict, word);
            word.remove(word.size() - 1);
        }
    }
}