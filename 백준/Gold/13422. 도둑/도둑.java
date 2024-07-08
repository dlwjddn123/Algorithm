import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int T = Integer.parseInt(st.nextToken());

        for (int i = 0; i < T; i++) {
            st = new StringTokenizer(br.readLine());
            int N = Integer.parseInt(st.nextToken());
            int M = Integer.parseInt(st.nextToken());
            int K = Integer.parseInt(st.nextToken());
            int[] houses = new int[N + 1];
            int result = 0;

            st = new StringTokenizer(br.readLine());
            for (int j = 1; j <= N; j++) {
                houses[j] = Integer.parseInt(st.nextToken()) + houses[j - 1];
            }

            if (N == M && houses[N] < K) {
                result = 1;
            } else {
                for (int l = 1; l <= N; l++) {
                    int p = (l + M - 1) % N;
                    int money = 0;
                    if (l > p) {
                        money = houses[N] - houses[l - 1] + houses[p];
                    } else {
                        money = houses[p] - houses[l - 1];
                    }

                    if (money < K) {
                        result += 1;
                    }
                }
            }

            System.out.println(result);
        }
    }
}
