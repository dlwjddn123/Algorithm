import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    static int N;
    static List<Integer>[] graph;
    static boolean[] visited;
    static int result = 0;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());
        visited = new boolean[N];
        graph = new ArrayList[N];

        for (int i = 0; i < N; i++) {
            graph[i] = new ArrayList<>();
        }

        for (int i = 0; i < M; i++) {
            st = new StringTokenizer(br.readLine());
            int p1 = Integer.parseInt(st.nextToken());
            int p2 = Integer.parseInt(st.nextToken());
            graph[p1].add(p2);
            graph[p2].add(p1);

        }
        for (int i = 0; i < N; i++) {
            if (result == 1) {
                break;
            }
            dfs(i, 1);
        }
        System.out.println(result);
    }
    public static void dfs(int idx, int depth) {
        if (depth == 5) {
            result = 1;
            return;
        }
        visited[idx] = true;
        for (int i : graph[idx]) {
            if (!visited[i]) {
                dfs(i, depth + 1);
            }
        }
        visited[idx] = false;
    }
}