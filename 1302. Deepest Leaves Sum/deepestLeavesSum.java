import java.util.ArrayList;
import java.util.List;
import java.util.Stack;

import org.junit.Test;

import org.junit.Assert;

/** 
 * LeetCode #1302: Deepest Leaves Sum (https://leetcode.com/problems/deepest-leaves-sum/)
 * Given the root of a binary tree, return the sum of values of its deepest leaves.
 */

class TreeNode {
    int val;
    TreeNode left;
    TreeNode right;
    TreeNode() {}
    TreeNode(int val) { this.val = val; }
    TreeNode(int val, TreeNode left, TreeNode right) {
        this.val = val;
        this.left = left;
        this.right = right;
    }
}

public class deepestLeavesSum {
    int maxHeight = 0;
    int height = 0;
    int maxSum = 0;

    /*
    * I originally did an iterative approach, clueless to the more refined recursion approach.
    * After being reminded that recursion was a much better way to do this problem, I created a recursion version.
    */
    public int deepSum_original_no_recursion(TreeNode root) {
        int depth = 0, sum = 0;

        Stack<TreeNode> treeStack = new Stack<TreeNode>();
        List<TreeNode> visitedNodes = new ArrayList<TreeNode>();
        

        treeStack.add(root);
        while ( !treeStack.isEmpty() ) {
            while ( root.left != null && !visitedNodes.contains(root.left) ) {
                treeStack.add(root.left);
                root = root.left;
            }
            while ( root.right != null && !visitedNodes.contains(root.right) ) {
                treeStack.add(root.right);
                root = root.right;
            }
            if ( root.left == null && root.right == null ) {
                if ( !treeStack.isEmpty() ) {
                    // If there is a new, deeper depth, overwrite the depth and sum value.
                    if ( treeStack.size() > depth ) {
                        depth = treeStack.size();
                        sum = root.val;
                    }
                    else if ( treeStack.size() == depth ) {
                        sum += root.val;
                    }
                    visitedNodes.add(treeStack.pop());
                }                
                if ( !treeStack.isEmpty() ) {
                    root = treeStack.peek();
                }
            }
            /*
            * Handles the case where it's going down the right branch and the node has a null right child but unexplored left child.
            * This is caused when going down the right of root. Since it is going down every root.right, it will not go down root.left until the next iteration.
            * This is problematic because without this if, it will consider the deepest root.right as finished (without exploring any root.left) and pop.
            */
            else if ( !visitedNodes.contains(root.left) && !visitedNodes.contains(root.right) ) {
                continue;
            }
            else {
                if ( !treeStack.isEmpty() ) {
                    visitedNodes.add(treeStack.pop());
                }                
                if ( !treeStack.isEmpty() ) {
                    root = treeStack.peek();
                }
            }
        }

        return sum;
    }

    public void deepSum_recursion(TreeNode root, int height) {
        if ( root == null ) return;
        height += 1;
        deepSum_recursion(root.left, height);
        if ( root.left == null && root.right == null ) {
            if ( height > maxHeight ) {
                maxHeight = height;
                maxSum = root.val;
            }
            else if ( height == maxHeight ) {
                maxSum += root.val;
            }
        }
        deepSum_recursion(root.right, height);
    }

    public static void main(String[] args) {
        
    }
    
    @Test
    public void test1() {
        TreeNode root = new TreeNode(1);
        root.left = new TreeNode(2);
        root.left.left = new TreeNode(4, new TreeNode(7, null, null), null);
        root.left.right = new TreeNode(5, null, null);

        root.right = new TreeNode(3);
        root.right.left = null;
        root.right.right = new TreeNode(6, null, new TreeNode(8, null, null));

        Assert.assertEquals(15, deepSum_original_no_recursion(root));
        
        deepSum_recursion(root, 0);
        Assert.assertEquals(15, maxSum);
    }

    @Test
    public void test2() {
        TreeNode root = new TreeNode(37, new TreeNode(97, null, new TreeNode(13, null, null)), new TreeNode(18, new TreeNode(18, null, null), null));

        Assert.assertEquals(31, deepSum_original_no_recursion(root));

        deepSum_recursion(root, 0);
        Assert.assertEquals(31, maxSum);
    }
}

