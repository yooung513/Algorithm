package org.example.inflearn.sec04;

import java.util.*;
import java.io.*;

// 회의실 배정
public class Inflearn4_5 {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());

        List<int[]> meeting = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            String[] tmp = br.readLine().split(" ");
            int s = Integer.parseInt(tmp[0]);
            int e = Integer.parseInt(tmp[1]);
            meeting.add(new int[]{s, e});
        }

        meeting.sort(Comparator.comparingInt(a -> a[1]));

        int cnt = 0;
        int pre = 0;
        for (int i = 0; i < n; i++) {
            int[] tmp = meeting.get(i);
            int now = tmp[0];

            if (now >= pre) {
                cnt++;
                pre = tmp[1];
            }
        }

        System.out.println(cnt);
    }
}
