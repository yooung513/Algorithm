package main.java.org.example.inflearn.sec04;

import java.util.*;
import java.io.*;

// 이분검색
public class Inflearn4_1 {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] nm = br.readLine().split(" ");
        int n = Integer.parseInt(nm[0]);
        int m = Integer.parseInt(nm[1]);

        String[] strArr = br.readLine().split(" ");
        int[] arr = new int[n];
        for (int i = 0; i < n; i++) {
            arr[i] = Integer.parseInt(strArr[i]);
        }
        Arrays.sort(arr);

        int s = 0; int e = n-1;
        while (s <= e) {
            int mid = (s + e) / 2;

            if (arr[mid] == m) {
                System.out.println(mid + 1);
                break;
            } else if (arr[mid] < m) {
                s = mid + 1;
            } else {
                e = mid - 1;
            }
        }
    }
}
