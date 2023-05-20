
# 2. Add Two Numbers
# Medium

'''
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.
'''
 
'''
Example 1:(2->4->3) + (5->6->4)
Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.

Example 2:
Input: l1 = [0], l2 = [0]
Output: [0]

Example 3:
Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]
 

Constraints:
The number of nodes in each linked list is in the range [1, 100].
0 <= Node.val <= 9
It is guaranteed that the list represents a number that does not have leading zeros.
'''

# my solution
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        res1, res2 = 0,0
        step1, step2 = 0,0
        while l1:
            res1 += l1.val * (10**step1)
            step1 += 1
            l1 = l1.next
        while l2:
            res2 += l2.val * (10**step2)
            step2 += 1
            l2 = l2.next
        res = str(res1 + res2)

        dummy = ListNode()
        cur = dummy
        for i in res[::-1]:
            cur.next = ListNode(int(i))
            cur = cur.next
        return dummy.next
            
#neetcode solution
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        cur = dummy

        carry = 0 #进位
        while l1 or l2 or carry: #adding carry here is to avoid the edge case like 8+7 at end of linkedlist, if still have carry we need to add them up
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0

            # new digit
            val = v1 + v2 + carry
            # get the carry out
            carry = val // 10
            val = val%10
            cur.next = ListNode(val)

            # update ptrs
            cur = cur.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return dummy.next

