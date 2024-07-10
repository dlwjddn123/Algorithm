
import java.io.*;
import java.util.*;

public class Main {

    public static class Result {
        int solution1;
        int solution2;
        int density;

        public Result(int density) {
            this.density = density;
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        int[] numbers = new int[N];

        StringTokenizer st = new StringTokenizer(br.readLine());
        for (int i = 0; i < N; i++) {
            numbers[i] = Integer.parseInt(st.nextToken());
        }

        Result result = new Result(Integer.MAX_VALUE);
        for (int i = 0; i < N; i++) {
            int minDensityIdx = binarySearch(numbers[i], numbers);
            if (minDensityIdx == -1) {
                continue;
            }
            int density = Math.abs(numbers[i] + numbers[minDensityIdx]);
            if (density < result.density) {
                result.solution1 = i;
                result.solution2 = minDensityIdx;
                result.density = density;
            }
        }

        System.out.println(Math.min(numbers[result.solution1], numbers[result.solution2]) + " " + Math.max(numbers[result.solution1], numbers[result.solution2]));
    }

    public static int binarySearch(int number, int[] numbers) {
        int start = 0;
        int end = numbers.length - 1;
        int minDensity = Integer.MAX_VALUE;
        int idx = -1;

        while (start <= end) {
            int mid = (start + end) / 2;
            if (minDensity > Math.abs(number + numbers[mid]) && number != numbers[mid]) {
                minDensity = Math.abs(number + numbers[mid]);
                idx = mid;
            }

            if (number < 0) {
                if (numbers[mid] < 0 && Math.abs(number) > Math.abs(numbers[mid])) {
                    end = mid - 1;
                    continue;
                } else if (numbers[mid] >= 0 && Math.abs(number) < Math.abs(numbers[mid])) {
                    end = mid - 1;
                    continue;
                }
                start = mid + 1;
                continue;
            }

            if (numbers[mid] < 0 && Math.abs(number) < Math.abs(numbers[mid])) {
                start = mid + 1;
                continue;
            }
            end = mid - 1;
        }
        return idx;
    }
}
