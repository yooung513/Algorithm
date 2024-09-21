package main.java.org.example.inflearn.sec08;

import java.util.*;

// 네트워크 선 자르기
public class Inflearn8_1 {
    private static int[] dy2;
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();

        // Bottom-Up
        int[] dy1 = new int[n + 1];
        dy1[1] = 1;
        dy1[2] = 2;

        for (int i = 3; i < n + 1; i++) {
            dy1[i] = dy1[i - 1] + dy1[i - 2];
        }

        System.out.println(dy1[n]);


        // Top-Down
        dy2 = new int[n + 1];
        System.out.println(DFS(n));
    }

    public static int DFS(int len) {
        if (dy2[len] > 0) {
            return dy2[len];
        }

        if (len == 1 || len == 2) {
            return len;
        } else {
            dy2[len] = DFS(len - 1) + DFS(len - 2);
            return dy2[len];
        }
    }
}
