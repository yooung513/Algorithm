package main.java.org.example.inflearn.sec03;

import java.util.*;
import java.io.*;

// 격자판 최대합
public class Inflearn3_6 {
    public static void main(String[] args) throws Exception {
        int maxRowSum = 0;
        int maxColSum = 0;
        int maxRightSum = 0;
        int maxLeftSum = 0;

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        int[][] arr = new int[n][n];
        for (int i = 0; i < n; i++) {
            String[] tmpStr = br.readLine().split(" ");

            int tmpRow = 0;
            int tmpCol = 0;
            for (int j = 0; j < n; j++) {
                arr[i][j] = Integer.parseInt(tmpStr[j]);
                tmpRow += arr[i][j];

                if (i == j) maxLeftSum += arr[i][j];
                if (i + j == n-1) maxRightSum += arr[i][j];
            }

            if (tmpRow > maxRowSum) maxRowSum = tmpRow;
        }

        for (int j = 0; j < n; j++) {
            int tmpCol = 0;
            for (int i = 0; i < n; i++) {
                tmpCol += arr[i][j];
            }

            if (tmpCol > maxColSum) maxColSum = tmpCol;
        }

        System.out.print(Math.max( Math.max( Math.max(maxRowSum, maxColSum), maxLeftSum), maxRightSum ));

    }
}
