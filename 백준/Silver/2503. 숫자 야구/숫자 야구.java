import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;

public class Main {
    static class Answer {
        String number;
        int strike;
        int ball;

        public Answer(String number, int strike, int ball) {
            this.number = number;
            this.strike = strike;
            this.ball = ball;
        }

        public boolean isMatched(String input) {
            int strikeCount = 0;
            int ballCount = 0;

            for (int i = 0; i < input.length(); i++) {
                if (input.charAt(i) == number.charAt(i)) {
                    strikeCount += 1;
                    continue;
                }
                ballCount += (number.contains(String.valueOf(input.charAt(i)))) ? 1 : 0;
            }

            return (strikeCount == strike && ballCount == ball) ? true : false;
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        List<Answer> answers = new ArrayList<>();
        int count = 0;

        for (int i = 0; i < N; i++) {
            String[] input = br.readLine().split(" ");
            answers.add(new Answer(input[0], Integer.parseInt(input[1]), Integer.parseInt(input[2])));
        }

        for (int i = 1; i <= 9; i++) {
            for (int j = 1; j <= 9; j++) {
                if (j == i) continue;
                for (int k = 1; k <= 9; k++) {
                    boolean isPossible = true;
                    if (k == i || k == j) continue;
                    for (Answer answer : answers) {
                        if (!answer.isMatched(String.valueOf(i) + String.valueOf(j) + String.valueOf(k))) {
                            isPossible = false;
                        }
                    }
                    if (isPossible) count += 1;
                }
            }
        }

        System.out.println(count);
    }
}
