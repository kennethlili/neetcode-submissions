class UnionFind:
    def __init__(self,length):
        par= {}
        rank = {}
        for i in range(length):
            par[i] = i
            rank[i] = 0
        self.par = par
        self.rank = rank

    def find(self,n):
        if self.par[n] == n:
            return n
        self.par[n] = self.find(self.par[n])
        return self.par[n]

    def union(self,n1, n2):
        p1, p2 = self.find(n1),self.find(n2)
        if (p1 == p2):
            return False
        if(self.rank[p1] > self.rank[p2]):
            self.par[p2] = p1
        elif (self.rank[p1] <self.rank[p2]):
            self.par[p1] = p2
        else:
            self.par[p2] = p1
            self.rank[p1] += 1
        return True

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        uf = UnionFind(len(accounts))
        emailToId = {}
        for i in range(len(accounts)):
            acc = accounts[i]
            for email in acc[1::]:
                if email in emailToId:
                    uf.union(i, emailToId[email])
                else:
                    emailToId[email] = i
        
        idToEmailArr = defaultdict(list)
        for email, i in emailToId.items():
            id = uf.find(i)
            idToEmailArr[id].append(email)
        res = []
        for id, emails in idToEmailArr.items():
            innerArr = [accounts[id][0]] + sorted(emails)
            res.append(innerArr)
        return res






