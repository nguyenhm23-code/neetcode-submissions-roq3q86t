class Solution {
public:
    bool isnormal(char c){
        if (48 <= c && c <= 57 || 
            'a' <= c && c <= 'z'||
            'A' <= c && c <= 'Z'){
                return true;
            }else{
                return false;
            }
    }
    bool isPalindrome(string s) {
    int l = 0;
    int r = s.size() - 1;
    while(l<r){
        while(l<r && isnormal(s[l]) == false){
            l++;
        }
        while(l<r && isnormal(s[r]) == false ){
            r--;
        }
        if(tolower(s[l]) != tolower(s[r])){
            return false;
        }
        l++;
        r--;
    }
    return true;
    }
    
};
