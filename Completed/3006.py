class Solution:
    def beautifulIndices(self, s: str, a: str, b: str, k: int) -> List[int]:

        # find all occurrences of a
        a_indexes = []
        for i in range(len(s)-len(a)+1):
            if s[i:i+len(a)] == a:
                a_indexes.append(i)


        # find all occurences of b
        b_indexes = []
        for j in range(len(s)-len(b)+1):
            if s[j:j+len(b)] == b:
                b_indexes.append(j)

        # iterate through b-indexes and if we find an a-index within k then 
        # we'll add the a-index to the result
        beautiful = []
        
        a_i, b_j = 0,0
        while a_i < len(a_indexes) and b_j < len(b_indexes):
            if abs(b_indexes[b_j]-a_indexes[a_i]) <= k:
                    beautiful.append(a_indexes[a_i])
                    a_i+=1
            elif b_indexes[b_j] > a_indexes[a_i]:
                a_i +=1
            else:
                b_j+=1 
        

        return beautiful
                
        