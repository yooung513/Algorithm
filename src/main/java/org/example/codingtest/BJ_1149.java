package main.java.org.example.codingtest;

import java.util.*;
import java.io.*;

// RGB
public class BJ_1149 {
    static int n;
    static int[][] house;
    static int result = Integer.MAX_VALUE;


    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        n = Integer.parseInt(br.readLine());
        house = new int[n][3];
        for (int i = 0; i < n; i++){
            String[] data = br.readLine().split(" ");
            for (int j = 0; j < 3; j++) {
                house[i][j] = Integer.parseInt(data[j]);
            }
        }

        dpNext('R', house[0][0], 1);
        dpNext('G', house[0][1], 1);
        dpNext('B', house[0][2], 1);

        System.out.println(result);

    }

    public static void dpNext(char rgb, int val, int idx) {
        if (idx == n && result > val) {
            result = val;
        } else if (val < result) {
            switch (rgb) {
                case 'R' :
                    if (val + house[idx][1] < result) dpNext('G', val + house[idx][1], idx+1);
                    if (val + house[idx][2] < result) dpNext('B', val + house[idx][2], idx+1);
                    break;
                    
                case 'G' :
                    if (val + house[idx][0] < result) dpNext('R', val + house[idx][0], idx+1);
                    if (val + house[idx][2] < result) dpNext('B', val + house[idx][2], idx+1);
                    break;
                    
                case 'B' :
                    if (val + house[idx][0] < result) dpNext('R', val + house[idx][0], idx+1);
                    if (val + house[idx][1] < result) dpNext('G', val + house[idx][1], idx+1);
                    break;
            }
        }
    }
}
