class Solution:
    def lowestCommonAncestor(self, root, p, q):
        # If root is None, return None
        if root is None:
            return None

        # If root is either p or q, return root
        if root == p or root == q:
            return root

        # Search in left subtree
        left = self.lowestCommonAncestor(root.left, p, q)

        # Search in right subtree
        right = self.lowestCommonAncestor(root.right, p, q)

        # p and q found in different subtrees
        if left and right:
            return root

        # Return the side where a node was found
        if left:
            return left
        else:
            return right
        