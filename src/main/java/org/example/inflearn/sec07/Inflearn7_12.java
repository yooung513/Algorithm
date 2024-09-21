package main.java.org.example.inflearn.sec07;

import java.io.*;
import java.util.*;

// 단지 번호 붙이기
public class Inflearn7_12 {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        int[][] house = new int[n][n];
        boolean[][] visited = new boolean[n][n];
        for (int i = 0; i < n; i++) {
            String[] tmp = br.readLine().split(" ");
            for (int j = 0; j < n; j++) {
                house[i][j] = Integer.parseInt(tmp[j]);
            }
        }

        List<Integer> ans = new ArrayList<>();
        int[] dx = new int[]{-1, 0, 1, 0};
        int[] dy = new int[]{0, 1, 0, -1};
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                if (house[i][j] == 1 && !visited[i][j]) {
                    Deque<int[]> dq = new ArrayDeque<>();
                    dq.addLast(new int[]{i, j});
                    visited[i][j] = true;

                    int cnt = 0;
                    while (!dq.isEmpty()) {
                        cnt++;
                        int[] tmp = dq.pollFirst();
                        int x = tmp[0];
                        int y = tmp[1];

                        for (int z = 0; z < 4; z++) {
                            int xx = x + dx[z];
                            int yy = y + dy[z];

                            if (0 <= xx && xx < n &&
                                0 <= yy && yy < n &&
                                house[xx][yy] == 1 &&
                                !visited[xx][yy]) {

                                visited[xx][yy] = true;
                                dq.addLast(new int[]{xx, yy});
                            }
                        }
                    }
                    ans.add(cnt);
                }
            }
        }

        System.out.println(ans.size());
        Collections.sort(ans);
        for (int x : ans) {
            System.out.println(x);
        }
    }
}

/*
7
0110100
0110101
1110101
0000111
0100000
0111110
0111000
*/
