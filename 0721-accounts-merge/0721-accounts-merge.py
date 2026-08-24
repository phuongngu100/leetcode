class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        parent = [i for i in range(len(accounts))]

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
        
        def union(a,b):
            root_a = find(a)
            root_b = find(b)

            if root_a != root_b:
                parent[root_b] = root_a
        
        email_to_account = {}
        for i, acc in enumerate(accounts):
            for email in acc[1:]:
                if email in email_to_account:
                    union(i, email_to_account[email])
                else:
                    email_to_account[email] = i
        print(email_to_account)
        # go from roots to sets of emails
        groups = defaultdict(set)
        for i, acc in enumerate(accounts):
            root = find(i)
            for email in acc[1:]:
                groups[root].add(email)
        res = []
        for root, email in groups.items():
            name = accounts[root][0]
            res.append([name] + sorted(email))
        return res


 


        