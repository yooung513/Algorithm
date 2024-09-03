package org.example.inflearn.sec06;

import java.util.*;

// 수열 추측하기
public class Inflearn6_9 {
    private static int n;
    private static int f;
    private static int[] arr;
    private static boolean[] visited;
    private static int[] bin;

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        n = sc.nextInt();
        f = sc.nextInt();
        arr = new int[n];
        visited = new boolean[n + 1];


        setBin();
        dfs(0);
    }

    public static void dfs(int v) {
        if (v == n) {
            if (calculate() == f) {
                StringBuilder sb = new StringBuilder();
                for (int x : arr) {
                    sb.append(x).append(" ");
                }
                System.out.println(sb);

                System.exit(0);
            }

        } else {
            for (int i = 1; i <= n; i++) {
                if (!visited[i]) {
                    visited[i] = true;
                    arr[v] = i;
                    dfs(v + 1);
                    visited[i] = false;
                }
            }
        }
    }

    // 파스칼의 삼각형 -> 이항 계수와 arr 곱의 합과 값이 동일
    // 초기 값을 1로 설정한 후 다음 값은 조합 공식에 따라 계산해 준다.
    public static void setBin() {
        bin = new int[n];
        Arrays.fill(bin, 1);

        for (int i = 1; i < n; i++) {
            bin[i] = bin[i - 1] * (n - i) / i;
        }
    }

    public static int calculate() {
        int val = 0;
        for (int i = 0; i < n; i++) {
            val += bin[i] * arr[i];
        }

        return val;
    }
}
