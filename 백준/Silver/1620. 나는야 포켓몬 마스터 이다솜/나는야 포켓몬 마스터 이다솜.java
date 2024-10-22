import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.HashMap;
import java.util.Map;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());
        Map<String, Integer> nameMap = new HashMap<>();
        Map<Integer, String> numberMap = new HashMap<>();

        for (int i = 0; i < N; i++) {
            String name = br.readLine();
            nameMap.put(name, i + 1);
            numberMap.put(i + 1, name);
        }

        for (int i = 0; i < M; i++) {
            String input = br.readLine();
            if (input.matches("^[a-zA-Z]*")) {
                System.out.println(nameMap.get(input));
            } else if (input.matches("^[0-9]*")) {
                System.out.println(numberMap.get(Integer.parseInt(input)));
            }
        }
    }
}
