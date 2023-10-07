import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Collections;
import java.util.List;
import java.util.StringTokenizer;

public class Main {

    private static int N, L, result;
    private static List<Integer> leakPoints = new ArrayList<>();
    public static void main(String[] args) throws IOException {
        input();
        findMinTapeCount();
        System.out.println(result);
    }

    public static void input() throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        L = Integer.parseInt(st.nextToken());
        st = new StringTokenizer(br.readLine());
        for (int idx = 0; idx < N; idx++) {
            leakPoints.add(Integer.parseInt(st.nextToken()));
        }
        Collections.sort(leakPoints);
    }

    public static void findMinTapeCount() {
        double coverRange = 0;
        for (int point : leakPoints) {
            if (coverRange >= point + 0.5) continue;
            if (coverRange <= point - 0.5) {
                result += 1;
                coverRange = point - 0.5 + L;
                continue;
            }
            result += 1;
            coverRange += L;
        }
    }
}
