class Solution {
    public int[] solution(int n, long left, long right) {
        int size = (int) (right - left + 1);
        int[] answer = new int[size];
        int idx = 0;
        for (long i = left; i <= right; i++) {
            int a = (int) (i / n);
            if (a < (int) (i % n)) {
                a = (int) (i % n);
            }
            answer[idx] = a + 1;
            idx += 1;
        }
        
        return answer;
    }
}