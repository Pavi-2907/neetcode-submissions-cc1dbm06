class Solution:
    def customSortString(self, order: str, s: str) -> str:
        res = []
        for ch in order:
            for c in s:
                if c == ch:
                    res.append(c)
        for c in s:
            if c not in order:
                res.append(c)
        return "".join(res)

        