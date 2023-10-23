class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        output = []
        l = 0
        r = len(products)-1
        products.sort()

        for i in range(len(searchWord)):
            c = searchWord[i]
            while l<=r and (len(products[l]) <= i or products[l][i] != c):
                l+=1
            while l<=r and (len(products[r]) <= i or products[r][i] != c):
                r-=1
            
            remain = r - l + 1
            output.append([])

            for j in range(min(3, remain)):
                output[-1].append(products[l + j])

        return output

