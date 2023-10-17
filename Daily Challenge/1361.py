class Solution:
    def validateBinaryTreeNodes(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:
        hasParent = set(leftChild + rightChild)
        hasParent.discard(-1)

        if len(hasParent) == n:
            return False
        root = -1

        for i in range(n):
            if i not in hasParent:
                root = i
                break
        
        visited = set()
        def dfs(node):
            if node == -1:
                return True
            if node in visited:
                return False
            visited.add(node)
            
            return dfs(leftChild[node]) and dfs(rightChild[node])
        return dfs(root) and len(visited) == n
