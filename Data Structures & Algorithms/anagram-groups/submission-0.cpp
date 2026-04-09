class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
    map <string, vector<string>> mp;
    for (string x : strs){
        string tmp = x;
        sort(tmp.begin(), tmp.end());
        mp[tmp].push_back(x);
        }
    vector<vector<string>> res;
    for (auto it : mp){
        res.push_back(it.second);   
    }
    return res;
    }
};
