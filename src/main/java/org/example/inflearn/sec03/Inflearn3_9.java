package main.java.org.example.inflearn.sec03;

import java.util.*;
import java.io.*;

// 봉우리
public class Inflearn3_9 {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        // 봉우리 생성
        int n = Integer.parseInt(br.readLine());
        int[][] height = new int[n + 2][n + 2];
        for (int i = 1; i <= n; i++) {
            String[] tmp = br.readLine().split(" ");
            for (int j = 0; j < n; j++) {
                height[i][j + 1] = Integer.parseInt(tmp[j]);
            }
        }

        // 가장 높은 지 확인
        int cnt = 0;
        int[] dx = new int[] {-1, 0, 1, 0};
        int[] dy = new int[] {0, -1, 0, 1};
        for (int i = 1; i <= n; i++) {
            for (int j = 1; j <= n; j++) {
                boolean flag = true;
                int now = height[i][j];
                for (int k = 0; k < 4; k++) {
                    int next = height[i + dx[k]][j + dy[k]];
                    if (next > now) {
                        flag = false;
                        break;
                    }
                }

                if (flag) cnt++;
            }
        }

        System.out.println(cnt);

    }

}
