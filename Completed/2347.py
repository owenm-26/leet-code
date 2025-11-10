class Solution:
    def bestHand(self, ranks: List[int], suits: List[str]) -> str:

        # check suit
        suitCount = Counter(suits)
        if suitCount[suits[0]] == 5:
            return "Flush"

        # check 3 of a kind 
        rank_count = Counter(ranks)
        is_pair = False
        for key in rank_count.keys():
            if rank_count[key] >2:
                return "Three of a Kind"
            if rank_count[key] == 2:
                is_pair = True

        if is_pair:
            return "Pair"

        return "High Card"
        
        