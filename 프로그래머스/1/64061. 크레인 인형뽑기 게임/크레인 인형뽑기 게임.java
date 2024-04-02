import java.util.*;

class Solution {
    public static int[][] b;
    public static Stack<Integer> basket;
    
    public int solution(int[][] board, int[] moves) {
        int answer = 0;
        b = board;
        basket = new Stack<>();
        for (int move : moves) {
            int doll = pick(move-1);
            if (doll != 0) {
                answer += burst(doll);    
            }
        }
        return answer;
    }
    
    public int pick(int pos) {
        for (int row = 0; row < b.length; row++) {
            if (b[row][pos] != 0) {
                int temp = b[row][pos];
                b[row][pos] = 0;
                return temp;
            }
        }
        return 0;
    }
    
    public int burst(int doll) {
        if (!basket.isEmpty() && basket.peek() == doll) {
            basket.pop();
            return 2;
        }
        basket.push(doll);
        return 0;
    } 
}