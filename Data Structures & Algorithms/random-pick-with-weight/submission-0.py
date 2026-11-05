class Solution:

    def __init__(self, w: List[int]):

        self.prefix = []
        tot = 0
        for num in w:
            tot+=num
            self.prefix.append(tot)
        self.tot= tot
        
    def pickIndex(self) -> int:
        num =random.randint(1,self.tot)
        for i,value in enumerate(self.prefix):
            if num <= value:
                return i
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()