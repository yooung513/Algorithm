package main.java.org.example.inflearn.sec07;

import java.io.*;

// 등산 경로
public class Inflearn7_11 {
    private static int n;
    private static int[][] mountain;
    private static int[] end;
    private static int[] dx = new int[]{-1, 0, 1, 0};
    private static int[] dy = new int[]{0, 1, 0, -1};
    private static int cnt;

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        n = Integer.parseInt(br.readLine());
        mountain = new int[n][n];

        int[] start = new int[2];
        end = new int[2];
        int bottom = Integer.MAX_VALUE;
        int top = Integer.MIN_VALUE;
        for (int i = 0; i < n; i++) {
            String[] tmp = br.readLine().split(" ");

            for (int j = 0; j < n; j++) {
                int val = Integer.parseInt(tmp[j]);
                mountain[i][j] = val;

                if (bottom > val) {
                    bottom = val;
                    start[0] = i;
                    start[1] = j;
                }

                if (top < val) {
                    top = val;
                    end[0] = i;
                    end[1] = j;
                }
            }
        }

        findRoute(start[0], start[1]);
        System.out.println(cnt);
    }

    public static void findRoute(int x, int y) {
        if (x == end[0] && y == end[1]) {
            cnt++;

        } else {
            for (int i = 0; i < 4; i++) {
                int xx = x + dx[i];
                int yy = y + dy[i];

                if (0 <= xx && xx < n &&
                    0 <= yy && yy < n &&
                    mountain[xx][yy] > mountain[x][y]) {

                    findRoute(xx, yy);
                }
            }
        }
    }
}
