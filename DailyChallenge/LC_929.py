class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        res = set()
        
        for email in emails:
            # split by @
            localName, domainName = email.split('@') 
            # remove username .
            # remove strings after +
            tmp = ""
            for ch in localName:
                if ch == '.': 
                    pass
                elif ch == '+': 
                    break
                else:
                    tmp += ch
            res.add(tmp+"@"+domainName)
        print(res)
        return len(res)
