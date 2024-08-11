package org.example.inflearn.sec04;

import java.io.*;

// 창고 정리

public class Inflearn4_7 {
    static int l;
    static int[] box;

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        l = Integer.parseInt(br.readLine());
        box = new int[l];

        String[] tmp = br.readLine().split(" ");
        for (int i = 0; i < l; i++) {
            box[i] = Integer.parseInt(tmp[i]);
        }

        int m = Integer.parseInt(br.readLine());
        for (int i = 0; i < m; i++) {
            findMax();
            findMin();
        }

        int maxVal = 0;
        int minVal = 101;
        for (int i = 0; i < l; i++) {
            if (box[i] > maxVal) {
                maxVal = box[i];
            }

            if (box[i] < minVal) {
                minVal = box[i];
            }
        }

        System.out.println(maxVal - minVal);
    }

    public static void findMax() {
        int idx = 0;
        int val = 0;
        for (int i = 0; i < l; i++) {
            if (box[i] > val) {
                idx = i;
                val = box[i];
            }
        }
        box[idx] -= 1;
    }

    public static void findMin() {
        int idx = 0;
        int val = 101;
        for (int i = 0; i < l; i++) {
            if(box[i] < val) {
                idx = i;
                val = box[i];
            }
        }
        box[idx] += 1;
    }
}