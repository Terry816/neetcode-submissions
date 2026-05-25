class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        #collect all unique letters
        letters = set()
        for word in words:
            for ch in word:
                letters.add(ch)
        
        outdegree = defaultdict(set) #letter:{outgoing edges}
        indegree = {ch:0 for ch in letters} #letter: number of incoming edges

        for i in range(len(words)-1):
            w1, w2 = words[i], words[i+1]
            minLen = min(len(w1), len(w2))
            if len(w1) > len(w2) and w1[:minLen] == w2[:minLen]:
                return ""
            for j in range(minLen):
                if w1[j] != w2[j]:
                    if w2[j] not in outdegree[w1[j]]:
                        outdegree[w1[j]].add(w2[j])
                        indegree[w2[j]] += 1
                    break
        
        #kahn's indegree algorithm
        q = deque()
        res = []
        for l in indegree:
            if indegree[l] == 0:
                q.append(l)
        while q:
            node = q.popleft()
            res.append(node)
            for l in outdegree[node]:
                indegree[l] -= 1
                if indegree[l] == 0:
                    q.append(l)
        return "".join(res) if len(res) == len(letters) else ""
            

        