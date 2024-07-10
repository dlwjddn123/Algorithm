import java.util.*;
import java.io.*;

class Solution {
    public int solution(int[][] board, int[][] skill) {
        int answer = 0;
        int N = board.length;
        int M = board[0].length;
        int[][] prefixSumBoard = new int[N + 1][M + 1];
        
        for (int i = 0; i < skill.length; i++) {
            prefixSumBoard[skill[i][1]][skill[i][2]] += (skill[i][0] == 1) ? -skill[i][5] : skill[i][5];    
            prefixSumBoard[skill[i][1]][skill[i][4] + 1] += (skill[i][0] == 1) ? skill[i][5] : -skill[i][5];
            prefixSumBoard[skill[i][3] + 1][skill[i][2]] += (skill[i][0] == 1) ? skill[i][5] : -skill[i][5];
            prefixSumBoard[skill[i][3] + 1][skill[i][4] + 1] += (skill[i][0] == 1) ? -skill[i][5] : skill[i][5];
        }

        for (int i = 0; i < M; i++) {
            for (int j = 1; j < N; j++) {
                prefixSumBoard[j][i] += prefixSumBoard[j - 1][i];
            }
        }
        
        for (int i = 0; i < N; i++) {
            for (int j = 1; j < M; j++) {
                prefixSumBoard[i][j] += prefixSumBoard[i][j - 1];
            }
        }
        
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < M; j++) {
                if (board[i][j] + prefixSumBoard[i][j] > 0) {
                    answer += 1;
                }
            }
        }

        return answer;
    }
}