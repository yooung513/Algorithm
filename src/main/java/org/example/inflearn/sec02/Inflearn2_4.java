package main.java.org.example.inflearn.sec02;

import java.util.*;
import java.io.*;

// 대표값
public class Inflearn2_4 {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        String[] inLine = br.readLine().split(" ");
        int[] score = new int[n];
        int avg = 0;

        for (int i = 0; i < n; i++) {
            score[i] = Integer.parseInt(inLine[i]);
            avg += score[i];
        }
        avg = (int) Math.round(avg * 1.0 / n);

        int distance = 0;
        int stdIdx = 0;
        int stdVal = 0;
        Boolean flag = true;
        while (true) {
            for (int i = 0; i < n; i++) {
                if ( (score[i]-avg) == distance || (avg-score[i]) == distance) {
                    if (score[i] > stdVal) {
                        stdIdx = i;
                        stdVal = score[i];
                    }
                    flag = false;
                }
            }

            if (!flag) {
                break;
            } else {
                distance++;
            }
        }

        System.out.print(avg + " ");
        System.out.print(stdIdx + 1);
    }
}
