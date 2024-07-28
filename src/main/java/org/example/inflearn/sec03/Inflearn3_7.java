package main.java.org.example.inflearn.sec03;

import java.util.*;
import java.io.*;

// 사과나무 (다이아몬드)
public class Inflearn3_7 {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());

        int[][] apple = new int[n][n];
        for (int i = 0; i < n; i++) {
            String[] tmp = br.readLine().split(" ");

            for(int j = 0; j < n; j++) {
                apple[i][j] = Integer.parseInt(tmp[j]);
            }
        }

        int cnt = 0;
        int s = n/2; int e = n/2;
        for (int i = 0; i < n; i++) {

            if (i < n/2) {
                for (int x = s; x <= e; x++) {
                    cnt += apple[i][x];
                }
                s--;
                e++;

            } else {
                for (int x = s; x <= e; x++) {
                    cnt += apple[i][x];
                }
                s++;
                e--;
            }
        }

        System.out.println(cnt);
    }
}
