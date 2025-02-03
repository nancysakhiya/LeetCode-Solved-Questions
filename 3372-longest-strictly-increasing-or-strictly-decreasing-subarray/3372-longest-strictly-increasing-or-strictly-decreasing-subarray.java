class Solution {
    public int longestMonotonicSubarray(int[] nums) {
        int maxLength = 0;

        for(int start = 0; start < nums.length; start++){
            int currLength = 1;
            for(int i = start+1; i < nums.length; i++){
                if(nums[i] > nums[i-1]){
                    currLength++;
                }
                else{
                    break;
                }
            }
            maxLength = Math.max(maxLength, currLength);
        }

        for(int start = 0; start < nums.length; start++){
            int currLength = 1;
            for(int i = start+1; i < nums.length; i++){
                if(nums[i] < nums[i-1]){
                    currLength++;
                }
                else{
                    break;
                }
            }
            maxLength = Math.max(maxLength, currLength);
        }
        return maxLength;
    }
}