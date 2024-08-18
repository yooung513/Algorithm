package main.java.org.example.inflearn.sec05;

import java.util.*;
import java.io.*;

// 공주 구하기
public class Inflearn5_5 {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] nk = br.readLine().split(" ");
        int n = Integer.parseInt(nk[0]);
        int k = Integer.parseInt(nk[1]);

        Deque<Integer> dq = new ArrayDeque<>();
        for (int i = 1; i <= n; i++) {
            dq.addLast(i);
        }

        int cnt = 0;
        while (!(dq.size() == 1)) {
            int tmp = dq.pollFirst();
            cnt++;

            if (cnt == k) {
                cnt = 0;
            } else {
                dq.addLast(tmp);
            }
        }

        System.out.println(dq.getFirst());
    }
}
