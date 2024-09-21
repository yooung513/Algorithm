package main.java.org.example.inflearn.sec07;

import java.io.*;

// 사다리 타기
public class Inflearn7_16 {
    private static int[][] ladder = new int[10][10];

    private static boolean[][] visited;
    private static int[] dx = new int[]{0, 0, 1};
    private static int[] dy = new int[]{1, -1, 0};

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        for (int i = 0; i < 10; i++) {
            String[] tmp = br.readLine().split(" ");
            for (int j = 0; j < 10; j++) {
                ladder[i][j] = Integer.parseInt(tmp[j]);
            }
        }

        for (int i = 0; i < 10; i++) {
            visited = new boolean[10][10];

            visited[0][i] = true;
            if (goNext(0, i)) {
                System.out.println(i + 1);
                break;
            }
        }

    }

    public static boolean goNext(int x, int y) {
        if (x == 9) {
            if (ladder[x][y] == 2) return true;

            return false;
        } else {
            for (int i = 0; i < 3; i++) {
                int xx = x + dx[i];
                int yy = y + dy[i];

                if (0 <= xx && xx < 10 && 0 <= yy && yy < 10 &&
                    ladder[xx][yy] == 1 && !visited[xx][yy]) {
                    visited[xx][yy] = true;
                    goNext(xx, yy);
                    break;
                }
            }
        }
        return false;
    }
}

/*
1 0 1 0 0 1 0 1 0 1
1 0 1 1 1 1 0 1 0 1
1 0 1 0 0 1 0 1 0 1
1 0 1 0 0 1 0 1 1 1
1 0 1 0 0 1 0 1 0 1
1 0 1 1 1 1 0 1 0 1
1 0 1 0 0 1 0 1 1 1
1 1 1 0 0 1 0 1 0 1
1 0 1 0 0 1 1 1 0 1
1 0 1 0 0 2 0 1 0 1
 */