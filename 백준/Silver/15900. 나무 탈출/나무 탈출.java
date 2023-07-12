import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;
import java.util.StringTokenizer;

public class Main {
    static boolean[] visited;
    static List<List<Integer>> nodes;
    static int count, N;
    static StringTokenizer st;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        N = Integer.parseInt(br.readLine());
        nodes = new ArrayList<>();
        visited = new boolean[N + 1];
        for (int i = 0; i <= N; i++) {
            nodes.add(new ArrayList<>());
        }

        for (int i = 0; i < N-1; i++) {
            st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            nodes.get(a).add(b);
            nodes.get(b).add(a);
        }
        dfs(1, 0);
        if (count % 2 == 0) {
            System.out.println("No");
        } else {
            System.out.println("Yes");
        }
    }

    public static void dfs(int node, int cnt) {
        boolean isLeaf = true;
        visited[node] = true;
        for (int idx : nodes.get(node)) {
            if (!visited[idx]) {
                isLeaf = false;
                dfs(idx, cnt + 1);
            }
        }
        if (isLeaf) {
            count += cnt;
        }
    }
}
