class Solution {
public:
     vector<int> findSubtreeSizes(vector<int>& par, string s) {
        int n=par.size();
        vector<vector<int>> adj(n);
        vector<int> answer(n, 1);
        for (int i = 1; i < n; ++i)
            adj[par[i]].push_back(i);
        vector<int> npar = par;
        unordered_map<char, vector<int>> lastSeen;
        function<void(int)> reassignParents = [&](int node) {
            char c=s[node];
            if (!lastSeen[c].empty())
                npar[node] = lastSeen[c].back();
            lastSeen[c].push_back(node);
            for (int child :adj[node])
                reassignParents(child);
            lastSeen[c].pop_back();
        };
         reassignParents(0);
        vector<vector<int>> newAdj(n);
        for (int i = 1; i < n; ++i)
            newAdj[npar[i]].push_back(i);
        function<int(int)> computeSubtreesizes = [&](int node) {
            int size = 1;
            for (int child :newAdj[node])
                size += computeSubtreesizes(child);
            answer[node] = size;
            return size;
        };
        computeSubtreesizes(0);
        return answer;
}
    };
