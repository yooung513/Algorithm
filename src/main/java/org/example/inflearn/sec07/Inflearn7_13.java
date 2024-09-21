package main.java.org.example.inflearn.sec07;

import java.util.*;
import java.io.*;

// 섬나라 아일랜드
public class Inflearn7_13 {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        int[][] island = new int[n][n];
        boolean[][] visited = new boolean[n][n];
        for (int i = 0; i < n; i++) {
            String[] tmp = br.readLine().split(" ");
            for (int j = 0; j < n; j++) {
                island[i][j] = Integer.parseInt(tmp[j]);
            }
        }

        int[] dx = new int[]{-1, -1, 0, 1, 1, 1, 0, -1};
        int[] dy = new int[]{0, 1, 1, 1, 0, -1, -1, -1};
        int cnt = 0;
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                if (island[i][j] == 1 && !visited[i][j]) {
                    cnt++;
                    Deque<int[]> dq = new ArrayDeque<>();
                    dq.addLast(new int[]{i, j});

                    while (!dq.isEmpty()) {
                        int[] tmp = dq.pollFirst();
                        for (int z = 0; z < 8; z++) {
                            int x = tmp[0] + dx[z];
                            int y = tmp[1] + dy[z];

                            if (0 <= x && x < n &&
                                0 <= y && y < n &&
                                island[x][y] == 1 &&
                                !visited[x][y]) {

                                visited[x][y] = true;
                                dq.addLast(new int[]{x, y});
                            }
                        }
                    }
                }
            }
        }

        System.out.println(cnt);
    }
}
