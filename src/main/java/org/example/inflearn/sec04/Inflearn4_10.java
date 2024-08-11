package main.java.org.example.inflearn.sec04;

import java.io.*;

// 역수열
public class Inflearn4_10 {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        String[] tmp = br.readLine().split(" ");
        int[] arr = new int[n];
        for (int i = 0; i < n; i++) {
            arr[i] = Integer.parseInt(tmp[i]);
        }

        int[] res = new int[n];
        for (int i = 0; i < n; i++) {
            int cnt = 0;

            for (int j = 0; j < n; j++) {
                if (cnt == arr[i] && res[j] == 0) {
                    res[j] = i+1;
                    break;
                }

                if(res[j] == 0) cnt++;
            }
        }

        for (int x : res) {
            System.out.print(x + " ");
        }
    }
}

