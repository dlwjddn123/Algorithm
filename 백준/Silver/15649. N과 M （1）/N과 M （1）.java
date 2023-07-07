import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Stack;
import java.util.StringTokenizer;
import java.util.stream.Collectors;

public class Main {
    public static Stack<Integer> nums;
    public static int N, M;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());
        nums = new Stack<>();
        go(1);
    }

    public static void go(int num) {
        if (nums.size() == M) {
            System.out.println(nums.stream().map(n -> n.toString()).collect(Collectors.joining(" ")));
            return;
        }
        for (int i = 1; i <= N; i++) {
            if (!nums.isEmpty() && nums.contains(i)) {
                continue;
            }
            nums.push(i);
            go(num + 1);
            nums.pop();
        }
    }
}
