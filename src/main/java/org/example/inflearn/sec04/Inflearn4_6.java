package org.example.inflearn.sec04;

import java.util.*;
import java.io.*;

// 씨름 선수
public class Inflearn4_6 {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(br.readLine());
        List<int[]> men = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            String[] tmp = br.readLine().split(" ");
            int height = Integer.parseInt(tmp[0]);
            int weight = Integer.parseInt(tmp[1]);

            men.add(new int[]{height, weight});
        }

        men.sort(Comparator.comparingInt(a -> a[0]));

        int cnt = n;
        for (int i = 0; i < n; i++) {
            int nowW = men.get(i)[1];

            for (int j = i + 1; j < n; j++) {
                int nextW = men.get(j)[1];

                if(nowW < nextW) {
                    cnt--;
                    break;
                }
            }
        }

        System.out.println(cnt);

    }
}
