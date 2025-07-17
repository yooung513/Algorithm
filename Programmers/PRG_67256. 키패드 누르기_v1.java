import java.util.*;
import java.io.*;

class Solution {
    private int[] nowL = new int[] {3, 0};
    private int[] nowR = new int[] {3, 2};
    private int[][] keyPad;
    
    private Map<Integer, int[]> leftNum = new HashMap<>();
    private Map<Integer, int[]> rightNum = new HashMap<>();
    private Map<Integer, int[]> middleNum = new HashMap<>();

    private int[] dx = new int[] {-1, 0, 1, 0};
    private int[] dy = new int[] {0, 1, 0, -1};
    
    private StringBuilder sb = new StringBuilder();
    
    public String solution(int[] numbers, String hand) {
        setKeyPad();
        setLeftNum();
        setRightNum();
        setMiddleNum();
        
        for(int number : numbers) {
            // 1. 키패드 왼쪽
            if (leftNum.containsKey(number)) {
                sb.append("L");
                nowL = leftNum.get(number);
              
            // 2. 키패드 오른쪽
            } else if (rightNum.containsKey(number)) {
                sb.append("R");
                nowR = rightNum.get(number);
                
            // 3. 키패드 가운데
            } else {
                int leftCount = findCount(nowL, number);
                int rightCount = findCount(nowR, number);
                
                System.out.println("leftCount :::::: " + leftCount);
                System.out.println("rightCount :::::: " + rightCount);
                
                if(leftCount < rightCount) {
                    sb.append("L");
                    nowL = middleNum.get(number);
                    
                } else if (leftCount == rightCount) {
                    if("left".equals(hand)) {
                        sb.append("L");
                        nowL = middleNum.get(number);
                    } else {
                        sb.append("R");
                        nowR = middleNum.get(number);
                    }
                    
                } else {
                    sb.append("R");
                        nowR = middleNum.get(number);
                }
            }
        }
        return sb.toString();
    }
    
    private int findCount(int[] where, int num) {
        boolean[][] visited = new boolean[4][3];
        
        Deque<int[]> dq = new ArrayDeque<>();
        dq.addLast(new int[] {where[0], where[1], 1});
        
        while(!dq.isEmpty()) {
            int[] now = dq.pollFirst();
            int x = now[0];
            int y = now[1];
            int v = now[2];
            
            if(keyPad[x][y] == num) return v;
            
            for(int i = 0; i < 4; i++) {
                int xx = x + dx[i];
                int yy = y + dy[i];
                
                if (0 <= xx && xx < 4 && 0 <= yy && yy < 3 &&
                   !visited[xx][yy]) {
                    
                    visited[xx][yy] = true;
                    dq.addLast(new int[] {xx, yy, v+1});
                }
            }
        }
        
        return -1;
    }
    
    private void setKeyPad() {
        keyPad = new int[][] {
            {1, 2, 3},
            {4, 5, 6},
            {7, 8, 9},
            {-1, 0, -1}
        };
    }
    
    private void setLeftNum() {
        leftNum.put(1, new int[] {0, 0});
        leftNum.put(4, new int[] {1, 0});
        leftNum.put(7, new int[] {2, 0});
    }
    
    private void setRightNum() {
        rightNum.put(3, new int[] {0, 2});
        rightNum.put(6, new int[] {1, 2});
        rightNum.put(9, new int[] {2, 2});
    }
    
    private void setMiddleNum() {
        middleNum.put(2, new int[] {0, 1});
        middleNum.put(5, new int[] {1, 1});
        middleNum.put(8, new int[] {2, 1});
        middleNum.put(0, new int[] {3, 1});
    }
}
