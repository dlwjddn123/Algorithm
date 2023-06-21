import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Stack;

public class Main {
    static StringBuilder sb = new StringBuilder();
    static Stack<Integer> stack = new Stack<>();
    static int cnt = 0;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        for (int i = 0; i < N; i++) {
            int num = Integer.parseInt(br.readLine());
            if (num > cnt) {
                push(num);
            }
            if (num <= cnt) {
                if(!pop(num)) {
                    System.out.println("NO");
                    return;
                }
            }
        }
        System.out.println(sb);
    }
    public static void push(int num) {
        for (int i = cnt; i < num; i++) {
            cnt += 1;
            stack.push(cnt);
            sb.append("+" + "\n");
        }
    }

    public static boolean pop(int num) {
        while(!stack.isEmpty()) {
            Integer temp = stack.pop();
            if (temp < num) {
                return false;
            }
            sb.append("-" + "\n");
            if (temp == num) {
                return true;
            }
        }
        return false;
    }
}