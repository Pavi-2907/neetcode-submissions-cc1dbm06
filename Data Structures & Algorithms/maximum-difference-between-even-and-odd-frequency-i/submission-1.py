class Solution:
    def maxDifference(self, s: str) -> int:
        freq = Counter(s)
        ev_fr = []
        odd_fr = []
        for ch, count in freq.items():
            if count%2==0:
                ev_fr.append(count)
            else:
                odd_fr.append(count)
        max_fr = max(odd_fr)
        min_fr = min(ev_fr)

        return max_fr - min_fr

        