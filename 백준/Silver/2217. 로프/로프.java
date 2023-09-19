import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Collections;
import java.util.Comparator;
import java.util.List;

public class Main {

    private static int N;
    private static List<Integer> ropes = new ArrayList<>();

    public static void main(String[] args) throws IOException {
        input();
        System.out.println(getMaximumWeight());
    }

    public static void input() throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        N = Integer.parseInt(br.readLine());
        for (int idx = 0; idx < N; idx++) {
            ropes.add(Integer.parseInt(br.readLine()));
        }
    }

    public static int getMaximumWeight() {
        Collections.sort(ropes, Comparator.reverseOrder());
        int maxWeight = ropes.get(0);
        for (int idx = 1; idx < N; idx++) {
            int currentWeight = ropes.get(idx);
            if (maxWeight < currentWeight * (idx + 1)) {
                maxWeight = currentWeight * (idx + 1);
            }
        }
        return maxWeight;
    }

}