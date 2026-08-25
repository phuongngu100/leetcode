class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        parent = [i for i in range(len(accounts))]

        # union find to find the root of all these - root as in a same email address
        def find(x):
            if x != parent[x]:
                parent[x] = find(parent[x])
            return parent[x]
        def union(a,b): # group them into  a group
            root_a = find(a)
            root_b = find(b)
            if root_a != root_b: # if there root is differnt connect them
                parent[root_b] = root_a
        email_to_account = {}
        for i, acc in enumerate(accounts):
            for email in acc[1:]: # loop through just the emails
                if email in email_to_account: # check if this email appear in other account, if yes, then merge those 2 
                    union(i,email_to_account[email]) # we merge them first, the dictionary does not change but find function will figure it out later
                else:
                    email_to_account[email] = i
        # print(email_to_account)
        groups = defaultdict(set) # root --> all emails belongs to that groups
        for i, acc in enumerate(accounts):
            root = find(i) # find the root of those we just merge
            for email in acc[1:]: 
                groups[root].add(email)
        res = []
        for root, email in groups.items():
            name = accounts[root][0] #get the name
            res.append([name] + sorted(email))
        return res









        

 


        