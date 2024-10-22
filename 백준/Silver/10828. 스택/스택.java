import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
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
                        System.out.println(-1);
                    } else {
                        System.out.println(stack.get(stack.size() - 1));
                        stack.remove(stack.size() - 1);
                    }
                    break;
                case "size":
                    System.out.println(stack.size());
                    break;
                case "empty":
                    System.out.println((stack.isEmpty()) ? 1 : 0);
                    break;
                case "top":
                    System.out.println((stack.isEmpty()) ? -1 : stack.get(stack.size() - 1));
            }
        }
    }
}
