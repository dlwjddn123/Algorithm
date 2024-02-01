import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        int result = 0;

        for (int i = 0; i < N; i++) {
            List<Character> alpha = new ArrayList<>();
            StringTokenizer st = new StringTokenizer(br.readLine());
            String str = st.nextToken();
            char prev = ' ';
            for (int j = 0; j < str.length(); j++) {
                char currentChar = str.charAt(j);
                if (alpha.contains(currentChar)) {
                    if (prev != currentChar) {
                        prev = '#';
                        break;
                    }
                    continue;
                }
                alpha.add(currentChar);
                prev = currentChar;
            }
            if (prev != '#') {
                result += 1;
            }
        }
        System.out.println(result);
    }
}
