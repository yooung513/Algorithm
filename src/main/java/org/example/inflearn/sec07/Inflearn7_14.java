package main.java.org.example.inflearn.sec07;

import java.io.*;
import java.sql.Array;
import java.util.*;

// 안전영역
public class Inflearn7_14 {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        int[][] board = new int[n][n];

        int top = 0;
        for (int i = 0; i < n; i++) {
            String[] tmp = br.readLine().split(" ");
            for (int j = 0; j < n; j++) {
                board[i][j] = Integer.parseInt(tmp[j]);

                if (board[i][j] > top) {
                    top = board[i][j];
                }
            }
        }

        int[] dx = new int[]{-1, 0, 1, 0};
        int[] dy = new int[]{0, 1, 0, -1};
        int[] safety = new int[top + 1];
        for (int i = 1; i < top; i++) {
            int cnt = 0;
            boolean[][] visited = new boolean[n][n];
            Deque<int[]> dq = new ArrayDeque<>();

            for (int x = 0; x < n; x++) {
                for (int y = 0; y < n; y++) {
                    if (board[x][y] > i && !visited[x][y]) {
                        dq.addLast(new int[]{x, y});
                        visited[x][y] = true;

                        while (!dq.isEmpty()) {
                            int[] tmp = dq.pollFirst();

                            for (int z = 0; z < 4; z++) {
                                int xx = tmp[0] + dx[z];
                                int yy = tmp[1] + dy[z];

                                if (0 <= xx && xx < n &&
                                    0 <= yy && yy < n &&
                                    board[xx][yy] > i &&
                                    !visited[xx][yy]) {

                                    dq.addLast(new int[]{xx, yy});
                                    visited[xx][yy] = true;
                                }
                            }
                        }
                        cnt++;
                    }

                    safety[i] = cnt;
                }
            }
        }

        int ans = 0;
        for (int i = 1; i <= top; i++) {
            if (safety[i] > ans) {
                ans = safety[i];
            }
        }

        System.out.println(ans);

    }
}

/*
5
6 8 2 6 2
3 2 3 4 6
6 7 3 3 2
7 2 5 3 6
8 9 5 2 7
* */