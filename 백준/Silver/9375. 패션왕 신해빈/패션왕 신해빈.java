import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int T = Integer.parseInt(br.readLine());

        for (int i = 0; i < T; i++) {
            System.out.println(solution(br));
        }
    }

    public static int solution(BufferedReader br) throws IOException {
        int N = Integer.parseInt(br.readLine());
        int result = 1;

        Map<String, Integer> clothesMap = new HashMap<>();

        for (int i = 0; i < N; i++) {
            String[] clothes = br.readLine().split(" ");
            if (clothesMap.containsKey(clothes[1])) {
                clothesMap.put(clothes[1], clothesMap.get(clothes[1]) + 1);
                continue;
            }
            clothesMap.put(clothes[1], 1);
        }

        for (int count : clothesMap.values()) {
            result *= (count + 1);
        }

        return result - 1;
    }

}
