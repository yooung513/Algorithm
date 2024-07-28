package main.java.org.example.inflearn.sec03;

import java.util.*;
import java.io.*;

// 수들의 합
public class Inflearn3_5 {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] nm = br.readLine().split(" ");
        int n = Integer.parseInt(nm[0]);
        int m = Integer.parseInt(nm[1]);

        String[] sArr = br.readLine().split(" ");
        int[] arr = new int[n];
        for (int i = 0; i < n; i++) {
            arr[i] = Integer.parseInt(sArr[i]);
        }

        int cnt = 0;
        for (int s = 0; s < n; s++) {
            int tmp = arr[s];

            if (tmp == m) {
                cnt++;
            } else if (tmp < m) {
                for (int e = s+1; e < n; e++) {
                    tmp += arr[e];

                    if (tmp == m) {
                        cnt++;
                        break;
                    } else if (tmp > m) {
                        break;
                    }
                }
            }
        }

        System.out.println(cnt);
    }
}
