import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());
        int[] nums = new int[N];
        int[] prefixSum = new int[N];

        st = new StringTokenizer(br.readLine());
        nums[0] = Integer.parseInt(st.nextToken());
        prefixSum[0] = nums[0];
        for (int i = 1; i < N; i++) {
            nums[i] = Integer.parseInt(st.nextToken());
            prefixSum[i] = nums[i] + prefixSum[i - 1];
        }
        for (int i = 0; i < M; i++) {
            st = new StringTokenizer(br.readLine());
            int start = Integer.parseInt(st.nextToken());
            int end = Integer.parseInt(st.nextToken());
            if (start == 1) {
                System.out.println(prefixSum[end - 1]);
                continue;
            }
            System.out.println(prefixSum[end - 1] - prefixSum[start - 2]);
        }
    }
}