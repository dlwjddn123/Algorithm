import java.util.*;

class Solution {
    public int solution(int alp, int cop, int[][] problems) {
        int maxAlp = 0;
        int maxCop = 0;
        for (int[] problem : problems) {
            maxAlp = Math.max(maxAlp, problem[0]);
            maxCop = Math.max(maxCop, problem[1]);
        }
        if (alp >= maxAlp && cop >= maxCop) {
            return 0;    
        }
        
        if (alp >= maxAlp) {
            alp = maxAlp;
        }
        
        if (cop >= maxCop) {
            cop = maxCop;
        }
        
        int[][] dp = new int[maxAlp + 2][maxCop + 2];
        for (int i = 0; i < dp.length; i++) {
            Arrays.fill(dp[i], Integer.MAX_VALUE);   
        }
        dp[alp][cop] = 0;
        
        for (int i = alp; i <= maxAlp; i++) {
            for (int j = cop; j <= maxCop; j++) {
                dp[i][j + 1] = Math.min(dp[i][j + 1], dp[i][j] + 1);
                dp[i + 1][j] = Math.min(dp[i + 1][j], dp[i][j] + 1);
                
                for (int[] problem : problems) {
                    if (i >= problem[0] && j >= problem[1]) {
                        if (i + problem[2] > maxAlp && j + problem[3] > maxCop) {
                            dp[maxAlp][maxCop] = Math.min(dp[maxAlp][maxCop], dp[i][j] + problem[4]);
                        } else if (i + problem[2] > maxAlp) {
                            dp[maxAlp][j + problem[3]] = Math.min(dp[maxAlp][j + problem[3]], dp[i][j] + problem[4]);
                        } else if (j + problem[3] > maxCop) {
                            dp[i + problem[2]][maxCop] = Math.min(dp[i + problem[2]][maxCop], dp[i][j] + problem[4]);
                        } else if (i + problem[2] <= maxAlp && j + problem[3] <= maxCop) {
                            dp[i + problem[2]][j + problem[3]] = Math.min(dp[i + problem[2]][j + problem[3]], dp[i][j] + problem[4]);
                        } 
                    }
                }
            }
        }
        return dp[maxAlp][maxCop];
    }
}