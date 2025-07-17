import java.util.*;
import java.io.*;

class Solution {
    private int[][] keyPad;
    
    public String solution(int[] numbers, String hand) {
        setKeyPad();
        int[] leftHand = new int[] {3, 0};
        int[] rightHand = new int[] {3, 2};
        
        StringBuilder sb = new StringBuilder();
        for(int number : numbers) {
            int[] pos = keyPad[number];
            
            // 1. 왼쪽 키패드
            if(number % 3 == 1) {
                sb.append("L");
                leftHand = pos;
                
            // 2. 오른쪽 키패드
            } else if(number % 3 == 0 && number != 0) {
                sb.append("R");
                rightHand = pos;
                
            // 3. 가운데 키패드
            } else {
                int leftDist = findDist(leftHand, pos);
                int rightDist = findDist(rightHand, pos);
                
                if(leftDist < rightDist) {
                    sb.append("L");
                    leftHand = pos;
                    
                } else if (rightDist < leftDist) {
                    sb.append("R");
                    rightHand = pos;
                    
                } else {
                    if("left".equals(hand)) {
                        sb.append("L");
                        leftHand = pos;
                        
                    } else {
                        sb.append("R");
                        rightHand = pos;
                        
                    }
                }
            }
        }
        
        return sb.toString();
    }
    
    // 맨해튼 거리 공식
    private int findDist(int[] hand, int[] target) {
        return Math.abs(hand[0] - target[0]) + Math.abs(hand[1] - target[1]);
    }
    
    private void setKeyPad() {
        keyPad = new int[][] {
            {3, 1},                     // keyPad[0] ...
            {0, 0}, {0, 1}, {0, 2},
            {1, 0}, {1, 1}, {1, 2},
            {2, 0}, {2, 1}, {2, 2},
        };
    }
}
