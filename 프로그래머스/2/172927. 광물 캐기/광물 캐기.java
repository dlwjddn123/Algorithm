import java.util.*;
class Solution {
    public int solution(int[] picks, String[] minerals) {
        int answer = 0;
        int pickSum = 0;
        Integer[][] mineralSum = new Integer[minerals.length/5 +1][4];

        pickSum = picks[0] + picks[1] + picks[2];

        for(int i = 0; i< mineralSum.length; i++){
            mineralSum[i] = new Integer[] {0,0,0,0};
        }

        for(int i = 0; i<minerals.length; i++){
            if(pickSum*5 <= i)
                break;

            if(minerals[i].equals("diamond")){
                mineralSum[i/5][0] += 25;
                mineralSum[i/5][1]++;

            }
            else if(minerals[i].equals("iron")){
                mineralSum[i/5][0] += 5;
                mineralSum[i/5][2]++;
            }
            else{
                mineralSum[i/5][0] +=1;
                mineralSum[i/5][3]++;
            }     
        }

        Arrays.sort(mineralSum,(a,b) -> b[0] - a[0]);

        for(int i = 0; i<mineralSum.length; i++){
            if(picks[0] == 0 && picks[1] == 0 && picks[2] ==0)
                break;

            if(picks[0]>0){
                picks[0]-=1;
                answer += mineralSum[i][1] + mineralSum[i][2] + mineralSum[i][3];
            }
            else if(picks[1]>0){
                picks[1]-=1;
                answer += mineralSum[i][1]*5 + mineralSum[i][2] +  mineralSum[i][3];
            }
            else{
                picks[2]-=1;
                answer += mineralSum[i][1]*25 + mineralSum[i][2]*5 +  mineralSum[i][3];
            }
        }
        for (Integer[] m : mineralSum) {
            System.out.println(Arrays.toString(m));    
        }
        
        return answer;
    }
}