import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

class Applicant {
    private int resume;
    private int interview;

    public Applicant(int resume, int interview) {
        this.resume = resume;
        this.interview = interview;
    }

    public int getResume() {
        return resume;
    }

    public int getInterview() {
        return interview;
    }
}

public class Main {

    private static List<Applicant> applicants;
    private static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    private static StringTokenizer st;
    private static int N;

    public static void main(String[] args) throws IOException {
        run();
    }

    public static void run() throws IOException {
        int T = Integer.parseInt(br.readLine());
        for (int t = 0; t < T; t++) {
            input();
            System.out.println(getMaximumNewComerCount());
        }
    }

    public static void input() throws IOException {
        st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        applicants = new ArrayList<>();
        for (int idx = 0; idx < N; idx++) {
            st = new StringTokenizer(br.readLine());
            applicants.add(new Applicant(Integer.parseInt(st.nextToken()), Integer.parseInt(st.nextToken())));
        }
    }

    public static int getMaximumNewComerCount() {
        applicants.sort(Comparator.comparing(Applicant::getResume));
        int count = 1;
        int minInterviewRank = applicants.get(0).getInterview();

        for (int idx = 1; idx < applicants.size(); idx++) {
            if (applicants.get(idx).getInterview() < minInterviewRank) {
                count += 1;
                minInterviewRank = applicants.get(idx).getInterview();
            }
        }
        return count;
    }

}
