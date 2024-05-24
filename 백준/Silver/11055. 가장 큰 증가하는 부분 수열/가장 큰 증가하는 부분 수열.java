import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Collections;
import java.util.List;
import java.util.StringTokenizer;

public class Main {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        List<Integer> nums = new ArrayList<>();
        List<Integer> dp = new ArrayList<>();
        StringTokenizer st = new StringTokenizer(br.readLine());

        for (int i = 0; i < N; i++) {
            nums.add(Integer.parseInt(st.nextToken()));
        }

        for (int i = 0; i < N; i++) {
            dp.add(nums.get(i));
            for (int j = 0; j < i; j++) {
                if (nums.get(i) > nums.get(j)) {
                    dp.set(i, Math.max(dp.get(j) + nums.get(i), dp.get(i)));
                }
            }
        }

        System.out.println(Collections.max(dp));
    }
}
