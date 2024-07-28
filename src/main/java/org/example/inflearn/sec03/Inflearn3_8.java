package main.java.org.example.inflearn.sec03;

import java.util.*;
import java.io.*;

// 곶감
public class Inflearn3_8 {

    private static int n;
    private static List<Deque<Integer>> arrDq;
    private static int[][] arr;
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        // 격자 생성
        n = Integer.parseInt(br.readLine());
        arrDq = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            String[] tmp = br.readLine().split(" ");

            Deque<Integer> tmpDq = new ArrayDeque<>();
            for (int j = 0; j < n; j++) {
                tmpDq.addLast(Integer.parseInt(tmp[j]));
            }
            arrDq.add(tmpDq);

        }

        // 이동 생성
        int m = Integer.parseInt(br.readLine());
        int[][] needs = new int[m][3];
        for (int i = 0; i < m; i++) {
            String[] tmp = br.readLine().split(" ");

            for (int j = 0; j < 3; j++) {
                needs[i][j] = Integer.parseInt(tmp[j]);
            }
        }

        // 격자판 이동
        for (int i = 0; i < m; i++) {
            move(needs[i][0]-1, needs[i][1], needs[i][2]);
        }

        // 격자판 리스트화
        arr = new int[n][n];
        for (int i = 0; i < n; i++) {
            Deque<Integer> tmp = arrDq.get(i);
            int len = tmp.size();

            for (int j = 0; j < len; j++) {
                arr[i][j] = tmp.pollFirst();
            }
        }

        // 모래시계 영역 합
        int cnt = 0;
        int s = 0; int e = n-1;
        for (int i = 0; i < n; i++) {
            if (i < n/2) {
                for (int j = s; j <= e; j++) {
                    cnt += arr[i][j];
                }
                s++;
                e--;

            } else {
                for (int j = s; j <= e; j++) {
                    cnt += arr[i][j];
                }
                s--;
                e++;
            }
        }

        System.out.println(cnt);

    }

    public static void move(int row, int dir, int num) {
        Deque<Integer> dq = arrDq.get(row);

        for (int i = 0; i < num; i++) {
            if (dir == 0) {
                dq.addLast(dq.pollFirst());
            } else {
                dq.addFirst(dq.pollLast());
            }
        }
    }
}
