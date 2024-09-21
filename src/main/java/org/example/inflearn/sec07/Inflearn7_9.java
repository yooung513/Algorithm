package main.java.org.example.inflearn.sec07;

import java.io.*;
import java.util.*;

// 미로의 최단거리 통로 (BFS)
public class Inflearn7_9 {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int[][] board = new int[7][7];
        for (int i = 0; i < 7; i++) {
            String[] tmp = br.readLine().split(" ");
            for (int j = 0; j < 7; j++) {
                board[i][j] = Integer.parseInt(tmp[j]);
            }
        }

        int[] dx = new int[]{-1, 0, 1, 0};
        int[] dy = new int[]{0, 1, 0, -1};
        int[][] dis = new int[7][7];
        for (int i = 0; i < 7; i++) {
            Arrays.fill(dis[i], -1);
        }
        Deque<int[]> dq = new ArrayDeque<>();

        dq.addLast(new int[]{0, 0});
        dis[0][0] = 0;
        while(!dq.isEmpty()) {
            int[] now = dq.pollFirst();
            int x = now[0];
            int y = now[1];

            for (int i = 0; i < 4; i++) {
                int xx = x + dx[i];
                int yy = y + dy[i];

                if (0 <= xx && xx < 7 &&
                    0 <= yy && yy < 7 &&
                    board[xx][yy] == 0 &&
                    dis[xx][yy] == -1){

                    dis[xx][yy] = dis[x][y] + 1;
                    dq.addLast(new int[]{xx, yy});
                }
            }
        }

        System.out.println(dis[6][6]);
    }
}
