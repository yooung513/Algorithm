package main.java.org.example.inflearn.sec07;

import java.io.*;

// 미로탐색
public class Inflearn7_10 {
    private static int[][] board = new int[7][7];
    private static boolean[][] visited = new boolean[7][7];
    private static int[] dx = new int[]{-1, 0, 1, 0};
    private static int[] dy = new int[]{0, 1, 0, -1};
    private static int cnt;

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        for (int i = 0; i < 7; i++) {
            String[] tmp = br.readLine().split(" ");
            for (int j = 0; j < 7; j++) {
                board[i][j] = Integer.parseInt(tmp[j]);
            }
        }

        visited[0][0] = true;
        findRoute(0, 0);
        System.out.println(cnt);
    }

    public static void findRoute(int x, int y) {
        if (x == 6 && y == 6) {
            cnt++;

        } else {
            for (int i = 0; i < 4; i++) {
                int xx = x + dx[i];
                int yy = y + dy[i];

                if (0 <= xx && xx < 7 &&
                    0 <= yy && yy < 7 &&
                    board[xx][yy] == 0 &&
                    !visited[xx][yy]) {

                    visited[xx][yy] = true;
                    findRoute(xx, yy);
                    visited[xx][yy] = false;
                }
            }
        }
    }
}
