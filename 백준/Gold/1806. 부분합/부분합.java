

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());
        int S = Integer.parseInt(st.nextToken());

        int[] sequence = new int[N];
        int[] prefixSum = new int[N];

        st = new StringTokenizer(br.readLine());

        for (int i = 0; i < N; i++) {
            sequence[i] = Integer.parseInt(st.nextToken());
            prefixSum[i] = sequence[i];
        }

        for (int i = 1; i < N; i++) {
            prefixSum[i] += prefixSum[i - 1];
        }

        int p1 = 0;
        int p2 = 0;
        int minSeqLength = 100001;

        while (p1 <= p2 && p2 < N) {
            if (sequence[p2] >= S) {
                minSeqLength = 1;
                break;
            }
            if (prefixSum[p2] - prefixSum[p1] + sequence[p1] >= S) {
                minSeqLength = (minSeqLength > p2 - p1 + 1) ? p2 - p1 + 1 : minSeqLength;
                p1 += 1;
                continue;
            }
            p2 += 1;
        }
        if (minSeqLength > 100000) {
            System.out.println(0);
            return;
        }
        System.out.println(minSeqLength);
    }
}
