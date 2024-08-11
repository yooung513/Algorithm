package main.java.org.example.inflearn.sec04;

import java.util.*;
import java.io.*;

// 뮤직비디오
public class Inflearn4_3 {
    static int[] song;
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] nm = br.readLine().split(" ");
        int n = Integer.parseInt(nm[0]);
        int m = Integer.parseInt(nm[1]);

        String[] data = br.readLine().split(" ");
        song = new int[n];
        int maxCap = 0;
        for (int i = 0; i < n; i++) {
            song[i] = Integer.parseInt(data[i]);

            maxCap += song[i];
        }

        int s = 1; int e = maxCap;
        int cap = 0;
        while (s <= e) {
            int mid = (s + e) / 2;

            if (m >= checkCap(mid)) {
                cap = mid;
                e = mid - 1;

            } else {
                s = mid + 1;
            }
        }

        System.out.println(cap);
    }

    public static int checkCap(int cap) {
        int cnt = 0;
        int tmpCap = 0;

        for (int i = 0; i < song.length; i++) {
            int now = tmpCap + song[i];
            if (now > cap) {
                cnt++;
                tmpCap = song[i];
            } else {
                tmpCap += song[i];
            }
        }

        if (tmpCap > 0) cnt++;

        return cnt;
    }
}
