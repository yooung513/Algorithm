import java.util.*;
import java.io.*;

class Solution {
    private Map<Character, int[]> typeMap = new HashMap<>();
    
    public String solution(String[] survey, int[] choices) {
        setTypeMap();
        int[] type = new int[4];
        
        for(int i = 0; i < survey.length; i++) {
            char[] sur = survey[i].toCharArray();
            int[] choice = findChoice(choices[i]);
                        
            char character = sur[choice[0]];
            int score = choice[1];

            int[] check = typeMap.get(character);
            type[check[0]] += score * check[1];
        }
        
        StringBuilder sb = new StringBuilder();
        sb.append(type[0] >= 0 ? "R" : "T");
        sb.append(type[1] >= 0 ? "C" : "F");
        sb.append(type[2] >= 0 ? "J" : "M");
        sb.append(type[3] >= 0 ? "A" : "N");

        return sb.toString();
    }
    
    private int[] findChoice(int choice) {
        if (choice == 4) return new int[] {0, 0};
        if (choice < 4) return new int[] {0, 4 - choice};
        return new int[] {1, choice - 4};
    }
    
    private void setTypeMap() {
        typeMap.put('R', new int[] {0, 1}); typeMap.put('T', new int[] {0, -1});
        typeMap.put('C', new int[] {1, 1}); typeMap.put('F', new int[] {1, -1});
        typeMap.put('J', new int[] {2, 1}); typeMap.put('M', new int[] {2, -1});
        typeMap.put('A', new int[] {3, 1}); typeMap.put('N', new int[] {3, -1});
    }
}
