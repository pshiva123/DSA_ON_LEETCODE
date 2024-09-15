class Solution {
public:
    struct Trie {
        vector<vector<int>> nodes;
        Trie() : nodes(1, vector<int>(26, -1)) {}
        void ins(const string& w) {
            int cur = 0;
            for (char c : w) {
                int idx = c - 'a';
                if (nodes[cur][idx] == -1) {
                    nodes[cur][idx] = nodes.size();
                    nodes.push_back(vector<int>(26, -1));
                }
                cur = nodes[cur][idx];
            }
        }
        void find(const string& t, int start, vector<int>& dp) {
            int cur = 0;
            for (int i = start; i < t.size(); ++i) {
                int idx = t[i] - 'a';
                if (nodes[cur][idx] == -1)
                    return;
                cur = nodes[cur][idx];
                dp[i + 1] = min(dp[i + 1], dp[start] + 1);
            }
        }
    };
    int minValidStrings(vector<string>& words, string target) {
        Trie trie;
        for (const string& w : words) {
            trie.ins(w);
        }
        int n = target.size();
        vector<int> dp(n + 1, numeric_limits<int>::max());
        dp[0] = 0;
        for (int i = 0; i < n; ++i) {
            if (dp[i] != numeric_limits<int>::max()) {
                trie.find(target, i, dp);
            }
        }
        return dp[n] == numeric_limits<int>::max() ? -1 : dp[n];
    }
};
