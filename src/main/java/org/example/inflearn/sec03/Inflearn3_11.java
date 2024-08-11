package main.java.org.example.inflearn.sec03;

import java.util.*;
import java.io.*;

// 격자판 회문수
public class Inflearn3_11 {
    static int[][] arr = new int[7][7];
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        for (int i = 0; i < 7; i++) {
            String[] tmp = br.readLine().split(" ");

            for (int j = 0; j < 7; j++) {
                arr[i][j] = Integer.parseInt(tmp[j]);
            }
        }

        int cnt = 0;
        for (int i = 0; i < 7; i++) {
            for (int j = 0; j < 3; j++) {
                if (checkRow(i, j)) cnt++;
                if (checkCol(j, i)) cnt++;
            }
        }

        System.out.println(cnt);
    }

    public static boolean checkRow(int row, int col) {
        for (int i = 0; i < 2; i++) {
            if (arr[row][col + i ] != arr[row][col + 4 - i])
                return false;
        }
        return true;
    }

    public static boolean checkCol(int row, int col) {
        for (int i = 0; i < 2; i++) {
            if (arr[row + i][col] != arr[row + 4 - i][col])
                return false;
        }
        return true;
    }

}
