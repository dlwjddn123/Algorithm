import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());

        for (int i = 0; i < N; i++) {
            String input = br.readLine();
            System.out.println(solution(input));
        }
    }

    public static String solution(String s) {
        int count = 0;

        for (int i = 0; i < s.length(); i++) {
            if (s.charAt(i) == '(') {
                count += 1;
            } else if (s.charAt(i) == ')') {
                count -= 1;
            }

            if (count < 0) {
                break;
            }
        }

        return (count == 0) ? "YES" : "NO";
    }
}
