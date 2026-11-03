"""
adj:
n: [f]
h: [e]
r: [n]
e: [r]

[f, n,r,e,h]


"""


class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        adj = {ch: [] for word in words for ch in word}
        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i + 1]
            minLen = min(len(w1), len(w2))
            if len(w1) > len(w2) and w1[:minLen] == w2[:minLen]:
                return ""

            for k in range(len(w1)):
                if k >= len(w2):
                    break
                ch1, ch2 = w1[k], w2[k]
                if ch1 != ch2:
                    adj[ch1].append(ch2)
                    break
        visited = set()
        visiting = set()
        temp = []

        def dfs(ch):
            if ch in visiting:
                return False
            if ch in visited:
                return True
            visited.add(ch)
            visiting.add(ch)
            for nCh in adj[ch]:
                if not dfs(nCh):
                    return False
            visiting.remove(ch)
            temp.append(ch)
            return True

        for ch, _ in adj.items():
            if not dfs(ch):
                return ""
        res = ""
        for i in range(len(temp) - 1, -1, -1):
            res += temp[i]

        return res
