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
            boolean flagRow = true;
            for (int j = 0; j < 3; j++) {

                for (int k = 0; k < 2; k++) {
                    System.out.println(arr[i][j+k] + " / " + arr[i][4-j-k]);
                    if (arr[i][j+k] != arr[i][4-j-k]) {
                        flagRow = false;
                        break;
                    }
                }

            }
            if (flagRow) cnt++;
            System.out.println("cnt = " + cnt);
            System.out.println();
        }
        System.out.println(cnt);

        for (int i = 0; i < 3; i++) {
            for (int j = 0; j < 7; j++) {
                boolean flagCol = true;

                for (int k = 0; k < 2; k++) {
                    if (arr[j][i+k] != arr[j][4-i-k]) {
                        flagCol = false;
                        break;
                    }
                }

                if (flagCol) cnt++;
            }
        }

    }
}
