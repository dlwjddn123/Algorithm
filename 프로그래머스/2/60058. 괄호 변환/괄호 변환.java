import java.util.*;
import java.io.*;


class Solution {
    public String solution(String p) {
        String answer = adjust(p);
        return answer;
    }
    
    public static String adjust(String p) {
        StringBuilder result = new StringBuilder();
        String u = findU(p);
        String v = (u.length() != p.length()) ? p.substring(u.length()) : "";
        if (u == "") {
            return u;
        }

        if (isBalanced(u)) {
            result.append(u);
            if (v != "") {
                result.append(adjust(v));
            }
        } else {
            result = new StringBuilder();
            result.append("(").append(adjust(v)).append(")");
            String a = reverse(u.substring(1, u.length() - 1));
            result.append(a);
        }

        return result.toString();
    }
    
    public static String findU(String p) {
        int stack = 0;
        String u = "";

        for (int i = 0; i < p.length(); i++) {
            if (p.charAt(i) == '(') {
                stack += 1;
            } else if (p.charAt(i) == ')') {
                stack -= 1;
            }

            if (stack == 0) {
                u = p.substring(0, i + 1);
                break;
            }
        }

        return u;
    }
    
    public static boolean isBalanced(String p) {
        int stack = 0;

        for (int i = 0; i < p.length(); i++) {
            if (p.charAt(i) == '(') {
                stack += 1;
            } else if (p.charAt(i) == ')') {
                stack -= 1;
            }

            if (stack < 0) {
                return false;
            }
        }

        return true;
    }
    
    public static String reverse(String p) {
        StringBuilder result = new StringBuilder();

        for (int i = 0; i < p.length(); i++) {
            result.append((p.charAt(i) == '(') ? ')' : '(');
        }
        return result.toString();
    }
}