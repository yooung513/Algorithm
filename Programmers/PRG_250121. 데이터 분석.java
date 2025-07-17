import java.util.*;

class Solution {
    public Map<String, Integer> idxMap = new HashMap<>();
    
    public int[][] solution(int[][] data, String ext, int val_ext, String sort_by) {
        setMap();
        int filterIdx = idxMap.get(ext);
        int sortIdx = idxMap.get(sort_by);
        
        List<int[]> dataList = new ArrayList<>();
        for(int[] d : data) {
            if(d[filterIdx] > val_ext) continue;
            
            dataList.add(d);
        }
        
        Collections.sort(dataList, (a, b) -> Integer.compare(a[sortIdx], b[sortIdx]));
        
        int[][] answer = new int[dataList.size()][];
        for(int i = 0; i < dataList.size(); i++) {
            answer[i] = dataList.get(i);
        }
        
        return answer;
    }
    
    private void setMap() {
        idxMap.put("code", 0);
        idxMap.put("date", 1);
        idxMap.put("maximum", 2);
        idxMap.put("remain", 3);
    }
}
