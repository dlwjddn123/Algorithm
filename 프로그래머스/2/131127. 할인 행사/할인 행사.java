import java.util.*;
class Solution {
    public int solution(String[] want, int[] number, String[] discount) {
        int answer=0;
        
        List<String> arr=new ArrayList<>();
        for(int i=0;i<want.length;i++){
            for(int j=0;j<number[i];j++){
                arr.add(want[i]);
            }
        }
        
        for(int i=0;i<=discount.length-10;i++){
            
            List<String> t=new ArrayList<>(Arrays.asList(Arrays.copyOfRange(discount, i, i+10)));
            
            for(String a:arr){
                t.remove(String.valueOf(a));
            }
            if(t.isEmpty()){
                answer++;
            }
        }
        return answer;
    }
}