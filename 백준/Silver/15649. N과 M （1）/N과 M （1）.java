import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;
import java.util.stream.Collectors;

public class Main {
    public static int[] nums;
    public static boolean[] visited;
    public static int N, M, depth;
    public static StringBuilder sb;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());
        nums = new int[M];
        visited = new boolean[N + 1];
        sb = new StringBuilder();
        depth = 0;
        go(0);
        System.out.println(sb);
    }

    public static void go(int n) {
        if (depth == M) {
            for (int c : nums) {
                sb.append(c + " ");
            }
            sb.deleteCharAt(sb.length() - 1);
            sb.append("\n");
            return;
        }
        for (int i = 0; i < N; i++) {
            if (!visited[i]) {
                depth += 1;
                nums[n] = i + 1;
                visited[i] = true;
                go(n + 1);
                visited[i] = false;
                depth -= 1;
            }
        }
    }
}
