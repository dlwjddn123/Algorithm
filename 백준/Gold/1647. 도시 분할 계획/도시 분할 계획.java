

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    static int[][] graph;
    static int[] parent;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine(), " ");
        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());
        graph = new int[M][3];
        parent = new int[N+1];
        int total = 0;

        for (int i = 0; i < M; i++) {
            st = new StringTokenizer(br.readLine(), " ");
            graph[i][0] = Integer.parseInt(st.nextToken());
            graph[i][1] = Integer.parseInt(st.nextToken());
            graph[i][2] = Integer.parseInt(st.nextToken());
        }

        for (int i = 1; i < N+1; i++) {
            parent[i] = i;
        }

        Arrays.sort(graph, (o1, o2) -> {
            return o1[2] - o2[2];
        });
        int max = 0;

        for (int[] edge : graph) {
            if (find(edge[0]) != find(edge[1])) {
                total += edge[2];
                union(edge[0], edge[1]);
                max = edge[2];
            }
        }
        System.out.println(total - max);
    }

    public static int find(int x) {
        if (x == parent[x]) {
            return x;
        }
        parent[x] = find(parent[x]);
        return parent[x];
    }

    public static void union(int x, int y) {
        int xp = find(x);
        int yp = find(y);

        if (xp != yp) {
            parent[xp] = yp;
        }
    }
}
