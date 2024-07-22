package main.java.org.example.inflearn.sec03;

import java.util.*;
import java.io.*;

// 두 리스트 합치기
public class Inflearn3_4 {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(br.readLine());
        String[] strN = br.readLine().split(" ");
        int m = Integer.parseInt(br.readLine());
        String[] strM = br.readLine().split(" ");

        Deque<Integer> nList = new ArrayDeque<>();
        Deque<Integer> mList = new ArrayDeque<>();
        for (int i = 0; i < n; i++) {
            nList.addLast(Integer.parseInt(strN[i]));
        }
        for (int j = 0; j < m; j++) {
            mList.addLast(Integer.parseInt(strM[j]));
        }

        while (!nList.isEmpty() || !mList.isEmpty()) {
            int nFirst = nList.pollFirst();
            int mFirst = mList.pollFirst();

            if (nFirst <= mFirst) {
                mList.addFirst(mFirst);
                System.out.print(nFirst + " ");
            } else {
                nList.addFirst(nFirst);
                System.out.print(mFirst + " ");
            }

            if (nList.size() == 0) {
                while(!mList.isEmpty()) {
                    System.out.print(mList.pollFirst() + " ");
                }
            }
            if (mList.size() == 0) {
                while(!nList.isEmpty()) {
                    System.out.print(nList.pollFirst() + " ");
                }
            }
        }

    }
}
