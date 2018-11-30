class Solution(object):
    def numUniqueEmails(self, emails):
        """
        :type emails: List[str]
        :rtype: int
        """
        email_set = set([])
        for email in emails:
            domain = ""
            for c in email:
                if c == "+" or "@":
                    break
                
                elif c != ".":
                    domain += c
            
            local_name = email.split("@")[1]
            email_set.add(domain + local_name)
        
        return len(email_set)
            
            
