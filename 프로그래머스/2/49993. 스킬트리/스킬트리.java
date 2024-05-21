import java.util.*;

class Solution {
    public int solution(String skill, String[] skill_trees) {
        int impossible_skill_tree_count = 0;
        
        Map<Character, Integer> skill_order = new HashMap<>();
        
        for (int i = 0; i < skill.length(); i++) {
            skill_order.put(skill.charAt(i), i);
        }
        
        for (String skill_tree : skill_trees) {
            int idx = 0;
            for (int i = 0; i < skill_tree.length(); i++) {
                if (skill_order.containsKey(skill_tree.charAt(i))) {
                    if (skill_order.get(skill_tree.charAt(i)) == idx) {
                        idx += 1;
                        continue;
                    }
                    impossible_skill_tree_count += 1;
                    break;
                }
            }
        }
        
        return skill_trees.length - impossible_skill_tree_count;
    }
}