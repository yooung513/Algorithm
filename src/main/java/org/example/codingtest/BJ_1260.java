package main.java.org.example.codingtest;

import java.io.*;
import java.util.*;

// DFS와 BFS
public class BJ_1260 {

    // DFS, BFS 공통 사용 변수
    static int n, m, v;
    static int[][] arr;         // 그래프
    static boolean[] visited;   // 노드의 방문 여부 확인


    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        n = Integer.parseInt(st.nextToken());   // 정점(노드)의 개수
        m = Integer.parseInt(st.nextToken());   // 간선의 개수
        v = Integer.parseInt(st.nextToken());   // 시작 정점 번호

        arr = new int[n+1][n+1];
        visited = new boolean[n+1];

        for (int i = 0; i < m; i++) {
            StringTokenizer st_ = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st_.nextToken());
            int b = Integer.parseInt(st_.nextToken());

            arr[a][b] = 1;
            arr[b][a] = 1;
        }

        dfs(v);
        visited = new boolean[n+1];
        System.out.println();
        bfs(v);
    }

    public static void dfs(int v) {
        visited[v] = true;
        System.out.print(v + " ");
        for (int i = 1; i < n+1; i++) {
            if (arr[v][i] == 1 && visited[i] == false) {
                dfs(i);
            }
        }
    }

    public static void bfs(int v) {
        Deque<Integer> dq = new ArrayDeque<>();
        dq.addLast(v);
        visited[v] = true;
        while(!dq.isEmpty()) {
            int x = dq.pollFirst();
            System.out.print(x + " ");

            for (int i = 1; i < n+1; i++) {
                if (arr[x][i] == 1 && visited[i] == false) {
                    dq.addLast(i);
                    visited[i] = true;
                }
            }
        }
    }
}
