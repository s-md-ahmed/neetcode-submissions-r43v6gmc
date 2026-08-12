class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        unique_emails = set()
        
        for email in emails:
            
            local, domain = email.split('@')
            
            # Ignore everything after the first '+' in the local name
            if '+' in local:
                local = local.split('+')[0]
            
            # Remove all periods '.' from the local name
            local = local.replace('.', '')
            
            # Combine them back and add to the set
            unique_emails.add(local + '@' + domain)
            print(unique_emails)
            
        return len(unique_emails)