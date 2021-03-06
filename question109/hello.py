# 给定一个单元链表，元素按升序排序，将其转换为高度平衡的BST。
#
# 对于这个问题，一个高度平衡的二叉树是指：其中每个节点的两个子树的深度相差不会超过
# 1
# 的二叉树。
#
#
#
# 示例:
#
# 给定的排序链表： [-10, -3, 0, 5, 9],
#
# 则一个可能的答案是：[0, -3, 9, -10, null, 5]
#
# 0
# / \
#     -3
# 9
# / /
# -10
# 5


# 一种解决方案
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        if not head:
            return
        if not head.next:
            return TreeNode(head.val)
        # here we get the middle point,
        # even case, like '1234', slow points to '2',
        # '3' is root, '12' belongs to left, '4' is right
        # odd case, like '12345', slow points to '2', '12'
        # belongs to left, '3' is root, '45' belongs to right
        slow, fast = head, head.next.next
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        # tmp points to root
        tmp = slow.next
        # cut down the left child
        slow.next = None
        root = TreeNode(tmp.val)
        root.left = self.sortedListToBST(head)
        root.right = self.sortedListToBST(tmp.next)
        return root
