package org.example.inflearn.sec04;

import java.util.*;
import java.io.*;

// 침몰하는 타이타닉
public class Inflearn4_8 {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] nm = br.readLine().split(" ");
        int n = Integer.parseInt(nm[0]);
        int m = Integer.parseInt(nm[1]);

        List<Integer> menList = new ArrayList<>();
        String[] tmp = br.readLine().split(" ");
        for (int i = 0; i < n; i++) {
            menList.add(Integer.parseInt(tmp[i]));
        }

        menList.sort(Comparator.reverseOrder());
        int[] men = menList.stream().mapToInt(Integer::intValue).toArray();
        int cnt = 0;
        for (int i = 0; i < n; i++) {
            int weight = 0;
            if (men[i] > 0) {
                weight += men[i];
                men[i] = 0;

                for (int j = i + 1; j < n; j++) {
                    if (men[j] != 0 && weight + men[j] <= m) {
                        weight += men[j];
                        men[j] = 0;
                        break;
                    }
                }

                if (weight > 0) {
                    cnt++;
                }
            }
        }


        System.out.println(cnt);
    }
}
