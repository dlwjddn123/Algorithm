import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        for (int i = 0; i < N; i++) {
            String ps = br.readLine();
            int count = 0;
            for (char x : ps.toCharArray()) {
                if (x == '(') {
                    count += 1;
                } else {
                    count -= 1;
                    if (count < 0) {
                        break;
                    }
                }
            }
            if (count == 0) {
                System.out.println("YES");
            } else {
                System.out.println("NO");
            }
        }
    }
}