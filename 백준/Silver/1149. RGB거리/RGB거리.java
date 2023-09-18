import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Collections;
import java.util.List;
import java.util.StringTokenizer;

public class Main {
    private static int[][] house;
    private static int N;
    private static int RGB = 3;

    public static void main(String[] args) throws IOException {
        input();
        System.out.println(getMinimumCost());
    }

    public static void input() throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        N = Integer.parseInt(br.readLine());
        house = new int[N][RGB];
        for (int row = 0; row < N; row++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            for (int col = 0; col < 3; col++) {
                house[row][col] = Integer.parseInt(st.nextToken());
            }
        }
    }

    public static int getMinimumCost() {
        for (int idx = 0; idx < N - 1; idx++) {
            house[idx + 1][1] += Math.min(house[idx][0], house[idx][2]);
            house[idx + 1][0] += Math.min(house[idx][1], house[idx][2]);
            house[idx + 1][2] += Math.min(house[idx][0], house[idx][1]);
        }
        return Collections.min(List.of(house[N - 1][0], house[N - 1][1], house[N - 1][2]));
    }
}
