import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();
        int N = Integer.parseInt(br.readLine());
        List<Integer> stack = new ArrayList<>();

        for (int i = 0; i < N; i++) {
            String[] input = br.readLine().split(" ");
            switch (input[0]) {
                case "push":
                    stack.add(Integer.parseInt(input[1]));
                    break;
                case "pop":
                    if (stack.isEmpty()) {
                        sb.append("-1\n");
                    } else {
                        sb.append((stack.get(stack.size() - 1))).append("\n");
                        stack.remove(stack.size() - 1);
                    }
                    break;
                case "size":
                    sb.append(stack.size() + "\n");
                    break;
                case "empty":
                    sb.append((stack.isEmpty()) ? 1 : 0).append("\n");
                    break;
                case "top":
                    sb.append((stack.isEmpty()) ? -1 : stack.get(stack.size() - 1)).append("\n");
            }
        }
        System.out.println(sb.toString());
    }
}
