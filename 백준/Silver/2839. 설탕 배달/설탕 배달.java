import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        System.out.println(getMinimumBagCount(Integer.parseInt(br.readLine())));
    }

    public static int getMinimumBagCount(int N) {
        int count = 0;
        while (N >= 0) {
            if (N % 5 == 0) {
                count += N / 5;
                return count;
            }
            N -= 3;
            count += 1;
        }
        return -1;
    }
}
