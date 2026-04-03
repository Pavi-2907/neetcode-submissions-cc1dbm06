class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        u = set()
        for email in emails:
            local,domain = email.split('@')
            if '+' in local:
                local = local[:local.index('+')]
            local = local.replace('.','')

            n = local + '@' + domain
            u.add(n)
        return len(u)

        