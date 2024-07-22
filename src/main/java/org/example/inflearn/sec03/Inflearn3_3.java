package main.java.org.example.inflearn.sec03;

import java.util.*;
import java.io.*;

// 카드 역배치
public class Inflearn3_3 {
    static int[] card = new int[21];

    public static void main(String[] args) throws Exception {
        for (int i = 1; i <= 20; i++) {
            card[i] = i;
        }

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        for (int i = 1; i <= 10; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());

            int s = Integer.parseInt(st.nextToken());
            int e = Integer.parseInt(st.nextToken());

            change(s, e);
        }

        for(int i = 1; i <= 20; i++) {
            System.out.print(card[i] + " ");
        }
    }

    public static void change(int s, int e) {
        for (int i = 0; i <= (e - s)/2 ; i++) {
            int tmp = card[s+i];
            card[s+i] = card[e-i];
            card[e-i] = tmp;
        }
    }
}
