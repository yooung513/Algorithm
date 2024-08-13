package main.java.org.example.codingtest;

import java.util.*;

// 거리두기 확인하기
public class Pro_81302 {
    public static void main(String[] args) {
        int[] ans = Solution(new String[][]{{"POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"},
                {"POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"},
                {"PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"},
                {"OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"},
                {"PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"}});

        System.out.println(Arrays.toString(ans));
    }

    public static int[] Solution(String[][] places) {
        int[] answer = new int[5];
        for(int i = 0; i < 5; i++) {
            String[] now = places[i];
            String[][] place = new String[5][5];
            Deque<int[]> dq = new ArrayDeque<>();

            for (int x = 0; x < 5; x++) {
                String[] s = now[x].split("");

                for (int y = 0; y < 5; y++) {
                    place[x][y] = s[y];

                    if("P".equals(s[y])) {
                        dq.addLast(new int[] {x, y});
                    }
                }
            }

            int[] disX1 = new int[] {-1, 0, 1, 0};
            int[] disY1 = new int[] {0, 1, 0, -1};
            int[] disX2 = new int[] {-2, 0, 2, 0};
            int[] disY2 = new int[] {0, 2, 0, -2};
            int[] disX = new int[] {-1, -1, 1, 1};
            int[] disY = new int[] {-1, 1, 1, -1};
            int flag = 1;
            while(!dq.isEmpty()) {
                int[] tmp = dq.pollFirst();
                int nowX = tmp[0];
                int nowY = tmp[1];

                for (int z = 0; z < 4; z++) {
                    if(0 <= nowX + disX1[z] && nowX + disX1[z] < 5 &&
                        0 <= nowY + disY1[z] && nowY + disY1[z] < 5 &&
                        "P".equals(place[nowX + disX1[z]][nowY + disY1[z]]) ) {
                        flag = 0;
                        break;
                    }

                    if(0 <= nowX + disX[z] && nowX + disX[z] < 5 &&
                        0 <= nowY + disY[z] && nowY + disY[z] < 5 &&
                        "P".equals(place[nowX + disX[z]][nowY + disY[z]]) ) {
                        flag = 0;
                        break;
                    }

                    if(0 <= nowX + disX2[z] && nowX + disX2[z] < 5 &&
                        0 <= nowY + disY2[z] && nowY + disY2[z] < 5 &&
                        "P".equals(place[nowX + disX2[z]][nowY + disY2[z]]) &&
                        (!"X".equals(place[nowX + disX1[z]][nowY + disY1[z]])) ) {
                        flag = 0;
                        break;
                    }
                }

                if (flag == 0) break;
            }

            answer[i] = flag;
        }
        return answer;
    }
}
