class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        products.sort()
        res = []
        prefix = ""
        for ch in searchWord:
            prefix+=ch
            suggestion = []
            for product in products:
                if product.startswith(prefix):
                    suggestion.append(product)
                if len(suggestion) == 3:
                    break
            res.append(suggestion)
        return res                    
