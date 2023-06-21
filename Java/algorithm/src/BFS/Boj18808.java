package BFS;

import java.io.*;
import java.util.*;

public class Boj18808 {
    static int N, M, K, answer = 0;
    static int[][] map;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());
        K = Integer.parseInt(st.nextToken());
        map = new int[N][M];

        for (int n = 0; n < K; n++) {
            st = new StringTokenizer(br.readLine());
            int r = Integer.parseInt(st.nextToken());
            int c = Integer.parseInt(st.nextToken());
            int[][] sticker = new int[r][c];

            for (int i = 0; i < r; i++) {
                st = new StringTokenizer(br.readLine());
                for (int j = 0; j < c; j++) {
                    sticker[i][j] = Integer.parseInt(st.nextToken());
                }
            }
            go(sticker);
        }
        System.out.println(answer);
    }

    public static int[][] rotate(int[][] sticker) {
        int r = sticker.length;
        int c = sticker[0].length;
        int[][] result = new int[c][r];

        for (int i = 0; i < r; i++) {
            for (int j = 0; j < c; j++) {
                result[j][r-i-1] = sticker[i][j];
            }
        }
        return result;
    }

    public static List<List<Integer>> findPosition(int x, int y, int[][] sticker) {
        List<List<Integer>> position = new ArrayList<>();
        int r = sticker.length;
        int c = sticker[0].length;
        int nx = 0;
        int ny = 0;
        for (int i = 0; i < r; i++) {
            for (int j = 0; j < c; j++) {
                nx = x + j;
                ny = y + i;
                if (sticker[i][j] == 0) {
                    continue;
                }
                if ((0 <= nx && nx < M) && (0 <= ny && ny < N) && map[ny][nx] != 1) {
                    if (sticker[i][j] == 1) {
                        position.add(Arrays.asList(nx, ny));
                    }
                    continue;
                }
                return new ArrayList<>();
            }
        }
        return position;
    }

    public static void go(int[][] sticker) {
        List<List<Integer>> position;
        for (int n = 0; n < 4; n++) {
            for (int i = 0; i < N; i++) {
                for (int j = 0; j < M; j++) {
                    position = findPosition(j, i, sticker);
                    if (!position.isEmpty()) {
                        attach(position);
                        return;
                    }
                }
            }
            sticker = rotate(sticker);
        }
    }


    public static void attach(List<List<Integer>> position) {
        for (List<Integer> pos : position) {
            map[pos.get(1)][pos.get(0)] = 1;
            answer += 1;
        }
    }
}

