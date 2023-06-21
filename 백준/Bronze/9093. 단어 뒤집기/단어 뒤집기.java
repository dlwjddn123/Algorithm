import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    static StringBuilder sb = new StringBuilder();
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        for (int i = 0; i < N; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine(), " ");
            while (st.hasMoreTokens()) {
                reverse(st.nextToken());
            }
            sb.append("\n");
        }
        sb.deleteCharAt(sb.length() - 1);
        System.out.println(sb);
    }

    public static void reverse(String token) {
        String temp = "";
        for (int i = token.length()-1; i >= 0 ; i--) {
            temp += token.charAt(i);
        }
        sb.append(temp + " ");
    }
}