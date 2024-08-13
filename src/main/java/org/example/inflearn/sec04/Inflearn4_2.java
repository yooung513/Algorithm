package main.java.org.example.inflearn.sec04;

import java.util.*;
import java.io.*;

// 랜선 자르기
public class Inflearn4_2 {
    static int[] line;

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] kn = br.readLine().split(" ");
        int k = Integer.parseInt(kn[0]);
        int n = Integer.parseInt(kn[1]);

        line = new int[k];
        int maxL = 0;
        for (int i = 0; i < k; i++) {
            line[i] = Integer.parseInt(br.readLine());

            if (line[i] > maxL) maxL = line[i];
        }
        Arrays.sort(line);

        int s = 0; int e = maxL;
        int res = 0;
        while (s <= e) {
            int mid = (s + e) / 2;
            int cut = cutLine(mid);

            if (cut >= n) {
                res = mid;
                s = mid + 1;
            } else {
                e = mid - 1;
            }
        }
        System.out.println(res);
    }

    public static int cutLine(int len) {
        int cnt = 0;
        for (int i = 0; i < line.length; i++) {
            cnt += line[i] / len;
        }

        return cnt;
    }
}
