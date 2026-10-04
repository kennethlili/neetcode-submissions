# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if(not root):
            return False
        def dfs(node,sum):
            if not node:
                # if(targetSum == sum[0]):
                #     res[0] = True
                return False
            
            
            sum += node.val
            
            if not node.left and not node.right:
                print(sum)
                if(targetSum == sum):
                    print('found')
                    return True
                else:
                    return False
            return  dfs(node.left,sum) or dfs(node.right, sum)
            

        test =  dfs(root, 0)
        print(test)
        return test

        

        
      
      
    
        

        