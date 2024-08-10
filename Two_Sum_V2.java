import java.util.HashMap;

class Two_Sum_V2{

    public static void main(String[] args) {
        Solution sol = new Solution();
        
        int[] array = new int[]{2,7,11,15};
        int target = 9;
        int[] f = sol.twoSum(array, target);
        for(int x : f){
        System.out.println(x);
    }
}
}


class Solution {
    public int[] twoSum(int[] nums, int target) {
        
        HashMap<Integer,Integer> map = new HashMap<>();

        for(int i = 0;i<nums.length;i++){
            map.put(nums[i], i);

        }

        for(int i = 0;i<map.size();i++){

            int find = target-nums[i];
            if(map.containsKey(find)){
                int index = map.get(find);
                if(i == index ) continue;
                
                return new int[]{i,index};

            
            }
        }


        return new int[]{1,2,4,5,6,7,8,9};
    }
}