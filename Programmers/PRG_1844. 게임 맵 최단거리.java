import java.util.*;

class Solution {
    static class Node {
        int x, y, val;
        
        Node(int x, int y, int val) {
            this.x = x;
            this.y = y;
            this.val = val;
        }
    }
    
    public int solution(int[][] maps) {
        int n = maps.length - 1;
        int m = maps[0].length -1;
        
        int[] dx = new int[] {-1, 0, 1, 0};
        int[] dy = new int[] {0, 1, 0, -1};
        boolean[][] visited = new boolean[n+1][m+1];
        int res = Integer.MAX_VALUE;
        
        Deque<Node> dq = new ArrayDeque<>();
        dq.addLast(new Node(0, 0, 1));
        visited[0][0] = true;
        
        while(!dq.isEmpty()) {
            Node node = dq.pollFirst();
            
            if(node.x == n && node.y == m) {
                res = Math.min(res, node.val);
                break;
            }
            
            for(int i = 0; i < 4; i++) {
                int xx = node.x + dx[i];
                int yy = node.y + dy[i];
                
                if(0 <= xx && xx <= n && 0 <= yy && yy <= m &&
                  !visited[xx][yy] && maps[xx][yy] == 1) {
                    
                    visited[xx][yy] = true;
                    dq.addLast(new Node(xx, yy, node.val+1));
                }
            }
        }
        
        return res == Integer.MAX_VALUE ? -1 : res;
    }
}
