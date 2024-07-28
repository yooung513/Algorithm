package main.java.org.example.inflearn.sec03;

import java.util.*;
import java.io.*;

// 스도쿠 검사
public class Infearn3_10 {
    static int[][] sudoku = new int[9][9];

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        for (int i = 0; i < 9; i++) {
            String[] tmp = br.readLine().split(" ");

            for (int j = 0; j < 9; j++) {
                sudoku[i][j] = Integer.parseInt(tmp[j]);
            }
        }

        boolean flag = true;
        for (int i = 0; i < 9; i++) {
            if (!row(i)) flag = false;
            if (!col(i)) flag = false;

            if (!flag) break;
        }

            for (int i = 0; i < 9; i += 3) {
                if(!flag) break;

                for (int j = 0; j < 9; j += 3) {
                    if(!squre(i, j)) {
                        flag = false;
                        break;
                    }
                }
            }

        if(flag) {
            System.out.println("YES");
        } else {
            System.out.println("NO");
        }

    }

    public static boolean row(int c) {
        int[] chk = new int[10];

        for (int i = 0; i < 9; i++) {
            int tmp = sudoku[i][c];

            if (chk[tmp] == 0) {
                chk[tmp] = 1;
            } else {
                return false;
            }
        }

        return true;
    }

    public static boolean col(int r) {
        int[] chk = new int[10];

        for (int i = 0; i < 9; i++) {
            int tmp = sudoku[r][i];

            if (chk[tmp] == 0) {
                chk[tmp] = 1;
            } else {
                return false;
            }
        }

        return true;
    }

    public static boolean squre(int x, int y) {
        int[] chk = new int[10];
        for (int i = x; i < x+3; i++) {
            for (int j = y; j < y+3; j++) {
                int tmp = sudoku[i][j];

                if (chk[tmp] == 0) {
                    chk[tmp] = 1;
                } else {
                    return false;
                }
            }
        }

        return true;
    }
}
