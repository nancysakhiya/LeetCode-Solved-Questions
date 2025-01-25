class Solution {
    public int[] lexicographicallySmallestArray(int[] nums, int limit) {
        int n = nums.length;
        if(n == 0){
            return new int[0];
        }
        
        int[][] sortedPairwise = new int[n][2];
        for(int i = 0; i < n; i++){
            sortedPairwise[i][0] = nums[i];
            sortedPairwise[i][1] = i;
        }

        Arrays.sort(sortedPairwise, (a, b) -> Integer.compare(a[0], b[0]));

        int[] res = new int[n];
        int groupStart = 0;

        for (int i =0; i< n; i++){
            if(i == n-1 || sortedPairwise[i+1][0] - sortedPairwise[i][0] > limit){
                List<Integer> indices = new ArrayList<>();
                for(int j = groupStart; j<=i; j++){
                    indices.add(sortedPairwise[j][1]);
                }
                Collections.sort(indices);

                for(int j = 0; j < indices.size(); j++){
                    res[indices.get(j)] = sortedPairwise[groupStart + j][0];
                }

                groupStart = i + 1;
            }
        }
        return res;
    }
}