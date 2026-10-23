class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        adj = {n: set() for word in words for n in word}
        for i in range(len(words)-1):
            word1 = words[i]
            word2 = words[i+1]
            minLen = min(len(word1), len(word2))
            if (word1[:minLen] == word2[:minLen] and len(word1) > len(word2)):
                return "" 
            for k in range(len(word1)):
                if k >= len(word2):
                    break
                if word1[k] != word2[k]:
                    char = word1[k]
                    adj[char].add(word2[k])
                    break
        res = []
        visited = set()
        def dfs(n , cycle):
            if n in cycle:
                print('cycle')
                return -1
            if n in visited:
                return
           
            cycle.add(n)
            visited.add(n)
            if n in adj:
                for nei in adj[n]:
                    if dfs(nei, cycle) == -1:
                        return -1
            res.append(n)
            cycle.remove(n)
        for n in adj:
            if dfs(n, set()) == -1:
                return ""
        
        res.reverse()
        return "".join(res)

        

        

