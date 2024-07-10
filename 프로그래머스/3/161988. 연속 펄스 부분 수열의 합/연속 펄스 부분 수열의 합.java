import java.util.*;
import java.io.*;

class Solution {
    public long solution(int[] sequence) {
        long answer = 0;
        long[] dp = new long[sequence.length];
        long[] dp1 = new long[sequence.length];
        dp[0] = Math.max(dp[0], sequence[0] * -1);
        
        for (int i = 1; i < sequence.length; i++) {
            dp[i] = Math.max(dp[i - 1] + (sequence[i] * (long) Math.pow(-1, i - 1)), (sequence[i] * (long) Math.pow(-1, i - 1)));
        }
        
        dp1[0] = Math.max(dp1[0], sequence[0]);
        
        for (int i = 1; i < sequence.length; i++) {
            dp1[i] = Math.max(dp1[i - 1] + (sequence[i] * (long) Math.pow(-1, i)), (sequence[i] * (long) Math.pow(-1, i)));
        }
        
        System.out.println(Arrays.stream(dp).max().getAsLong());
        System.out.println(Arrays.stream(dp1).max().getAsLong());
        
        return Math.max(Arrays.stream(dp).max().getAsLong(), Arrays.stream(dp1).max().getAsLong());
    }
}