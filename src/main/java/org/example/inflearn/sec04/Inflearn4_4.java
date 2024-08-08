package org.example.inflearn.sec04;

import java.util.*;
import java.io.*;

// 마구간 정하기
public class Inflearn4_4 {

    static int[] house;

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        String[] nc = br.readLine().split(" ");
        int n = Integer.parseInt(nc[0]);
        int c = Integer.parseInt(nc[1]);

        house = new int[n];
        for (int i = 0; i < n; i++) {
            house[i] = Integer.parseInt(br.readLine());
        }

        Arrays.sort(house);
        int s = house[0]; int e = house[n-1] + 1;
        int distance = 0;
        while (s <= e) {
            int mid = (s + e) / 2;
            if (check(mid) >= c) {
                distance = mid;
                s = mid + 1;
            } else {
                e = mid - 1;
            }
        }

        System.out.print(distance);
    }


    public static int check(int dis) {
        int pre = house[0];
        int cnt = 1;
        for (int i = 1; i < house.length; i++) {
            int now = house[i];

            if (now - pre >= dis) {
                cnt++;
                pre = now;
            }
        }

        return cnt;
    }

}
