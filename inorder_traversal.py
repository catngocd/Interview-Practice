class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        inorder = []
        stack = []
        
        if root == None:
            return []
        
        while root != None or len(stack) > 0:
            while root != None:
                stack.append(root)
                root = root.left
            
            
            root = stack.pop()
            
            inorder.append(root.val)
            root = root.right
        
        return inorder
