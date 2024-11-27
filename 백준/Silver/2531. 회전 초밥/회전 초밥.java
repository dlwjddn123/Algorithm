import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] input = br.readLine().split(" ");
        int answer = 0;
        int N = Integer.parseInt(input[0]);
        int d = Integer.parseInt(input[1]);
        int k = Integer.parseInt(input[2]);
        int c = Integer.parseInt(input[3]);
        List<Integer> belt = new ArrayList<>();
        Map<Integer, Integer> sushi = new HashMap<>();
        int start = 0;
        int end = 0;


        for (int i = 0; i < N; i++) {
            belt.add(Integer.parseInt(br.readLine()));
        }

        sushi.put(belt.get(0), 1);
        sushi.put(c, 1);

        while (start < N) {
            if (end - start < k - 1) {
                end += 1;
                Integer current = belt.get(end);
                if (sushi.containsKey(current)) {
                    sushi.put(current, sushi.get(current) + 1);
                } else {
                    sushi.put(current, 1);
                }
                answer = (answer < sushi.keySet().size()) ? sushi.keySet().size() : answer;
                continue;
            }
            Integer startSushi = belt.get(start);
            if (sushi.get(startSushi) == 1) {
                sushi.remove(startSushi);
            } else {
                sushi.put(startSushi, sushi.get(startSushi) - 1);
            }
            start += 1;
            end += 1;
            Integer endSushi = belt.get(end % N);

            if (sushi.containsKey(endSushi)) {
                sushi.put(endSushi, sushi.get(endSushi) + 1);
            } else {
                sushi.put(endSushi, 1);
            }
            answer = (answer < sushi.keySet().size()) ? sushi.keySet().size() : answer;
        }

        System.out.println(answer);
    }
}
