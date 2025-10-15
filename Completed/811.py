from collections import defaultdict
class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        domainVisits = defaultdict(int)

        def partsIntoSubDomains(parts: list) -> list:
            res = []
            
            for i in range(len(parts)):
                res.append(".".join(parts[i:]))
            
            return res

        def processDomain(d:str) -> None:
            count, domain = d.split(" ")
            parts = domain.split(".")

            count = int(count)
            
            subDomains = partsIntoSubDomains(parts)

            for sub in subDomains:
                domainVisits[sub] += count

        # populates dict of counts
        for d in cpdomains:
            processDomain(d)

        # convert into strings and add to result
        ans = []
        for key, value in domainVisits.items():
            item = f"{value} {key}"
            ans.append(item)
        
        return ans
            

        