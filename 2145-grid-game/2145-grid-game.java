class Solution {
    public long gridGame(int[][] grid) {

        long minRes = Long.MAX_VALUE;
        long rowsum1 = 0;
        for(int i=0; i < grid[0].length; ++i){
           rowsum1 += grid[0][i];
        }

        long rowsum2 = 0;
        for(int i = 0; i < grid[0].length; ++i){
            rowsum1 -= grid[0][i];
            minRes = Math.min(minRes, Math.max(rowsum1, rowsum2));
            rowsum2 += grid[1][i];
        }

        return minRes;
    }
}