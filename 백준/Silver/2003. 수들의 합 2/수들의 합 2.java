import java.io.*;
import java.util.*;

public class Main {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());
        int[] numbers = new int[N + 1];

        st = new StringTokenizer(br.readLine());
        for (int i = 1; i < N + 1; i++) {
            numbers[i] = Integer.parseInt(st.nextToken()) + numbers[i - 1];
        }

        int p1 = 0;
        int p2 = 1;
        int result = 0;

        while (p1 <= p2 && p2 <= N) {
            if (numbers[p2] - numbers[p1] == M) {
                p1 += 1;
                result += 1;
                continue;
            }

            if (numbers[p2] - numbers[p1] < M) {
                p2 += 1;
                continue;
            }

            p1 += 1;
        }

        System.out.println(result);
    }
}
