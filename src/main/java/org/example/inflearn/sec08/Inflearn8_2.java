package main.java.org.example.inflearn.sec08;

import java.util.*;

// 계단 오르기
public class Inflearn8_2 {
    private static int[] dy;
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();

        dy = new int[n + 1];
        System.out.println(DFS(n));
    }

    public static int DFS(int len) {
        if (dy[len] > 0) {
            return dy[len];
        }

        if (len == 1 || len == 2) {
            return len;
        } else {
            dy[len] = DFS(len - 1) + DFS(len - 2);
            return dy[len];
        }
    }
}
