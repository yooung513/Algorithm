package org.example.codingtest;

import java.util.*;
import java.io.*;

// 거리두기 확인하기
// 맨해튼 거리 : (0, 2) (2, 0), (1, 1)  (1, 0) (0, 1)이면 거리두기 실패
public class Pro_81302 {
    public static void main(String[] arge) {
        Solution(new String[][]{{"POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"},
                                {"POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"},
                                {"PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"},
                                {"OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"},
                                {"PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"}});
    }

    static Deque<int[]> dq;
    static String[][] place;

    public static int[] Solution(String[][] places) {
        int[] answer = new int[5];
        for (int i = 0; i < 5; i++) {
            String[] tmp = places[i];
            place = new String[5][5];
            dq = new ArrayDeque<>();

            for (int x = 0; x < 5; x++) {
                String[] data = tmp[x].split("");

                for (int y = 0; y < 5; y++) {
                    String s = data[y];
                    place[x][y] = s;

                    if ("P".equals(s)) {
                        dq.addLast(new int[]{x, y});
                    }
                }
            }

            int[] dx = new int[]{-2, 0, 2, 0, -1, 0, 1, 0, -1, -1, 1, 1};
            int[] dy = new int[]{0, 2, 0, -2, 0, 1, 0, -1, -1, 1, 1, -1};
            boolean flag = true;
            while(!dq.isEmpty()) {
                int[] xy = dq.pollFirst();
                int x = xy[0];
                int y = xy[1];

                for (int z = 0; z < 12; z++) {
                    int xx = x + dx[z];
                    int yy = y + dy[z];
                    if (0 <= xx && xx < 5 && 0 <= yy && yy < 5
                            && "P".equals(place[xx][yy])) {
                        // 파티션 생각해야함 
                    }
                }
            }


        }


        return answer;
    }
}
