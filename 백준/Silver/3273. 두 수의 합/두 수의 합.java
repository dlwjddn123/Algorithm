import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        StringTokenizer st = new StringTokenizer(br.readLine());
        int[] nums = new int[N];

        for (int i = 0; i < N; i++) {
            nums[i] = Integer.parseInt(st.nextToken());
        }
        Arrays.sort(nums);

        int X = Integer.parseInt(br.readLine());

        int start = 0;
        int end = N-1;
        int count = 0;

        while (start < end) {
            int current = nums[start] + nums[end];
            if (current == X) {
                count += 1;
            }
            if (current <= X) {
                start += 1;
                continue;
            }
            end -= 1;
        }
        System.out.println(count);
    }
}