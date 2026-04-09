class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
    set<int> se;
    for (int &x: nums){
        se.insert(x);
    }
    if (se.size() == nums.size()){
        return false;
    }else{
        return true;
    }
    }
};