class Solution {
public:
    string breakPalindrome(string p) {
        if(p.length() == 1) {
            return "";
        }
        string ans = "";
        for(int i = 0; i < p.length()/2; i++) {
            for(int j = 0; j < 26; j++) {
                if(j + 'a' != p[i]) {
                    string tmp = p;
                    string tmp2 = p;
                    tmp[i] = j + 'a';
                    tmp2[p.length() - 1 - i] = j + 'a';
                    if(ans == "") {
                        ans = min(tmp,tmp2);
                    }
                    else {
                        if(ans > min(tmp,tmp2)) {
                            ans = min(tmp,tmp2);
                        }
                    }
                    break;
                }
            }
        }
        return ans;
    }
};