package org.example.inflearn.sec04;

import java.util.*;
import java.io.*;

// 증가수열 만들기
public class Inflearn4_9 {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        String[] tmp = br.readLine().split(" ");

        Deque<Integer> dq = new ArrayDeque<>();
        for (int i = 0; i < n; i++) {
            dq.add(Integer.parseInt(tmp[i]));
        }

        StringBuilder sb = new StringBuilder();
        int lastVal = 0;
        while (!dq.isEmpty()) {
            int l = dq.pollFirst();
            int r = 0;
            if (!dq.isEmpty()) {
                r = dq.pollLast();
            }

            if(l > lastVal && r > lastVal) {    // 양쪽 다 마지막 숫자보다 큰 경우
                if (l < r) {
                    sb.append("L");
                    dq.addLast(r);
                } else {
                    sb.append("R");
                    dq.addFirst(l);
                }
            } else if (l > lastVal) {           // 왼쪽만 큰 경우

            }


            // 오른쪽만 큰 경우

        }
    }
}
