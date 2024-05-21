import java.util.*;

class Solution {
    public static int MAX_LENGTH = 5;
    public static int number = -1;
    public static String[] alpha = new String[]{"A", "E", "I", "O", "U"};
    
    public int solution(String word) {
        Map<String, Integer> dict = new HashMap<>();
        
        recordOrderAllWordsToDict(dict, new StringBuilder());
        
        return dict.get(word);
    }
    
    public void recordOrderAllWordsToDict(Map<String, Integer> dict, StringBuilder word) {
        number += 1;
        dict.put(String.join("", word.toString()), number);
        
        if (word.length() == MAX_LENGTH) {
            return;
        }
        
        for (int i = 0; i < MAX_LENGTH; i++) {
            word.append(alpha[i]);
            recordOrderAllWordsToDict(dict, word);
            word.deleteCharAt(word.length() - 1);
        }
    }
}