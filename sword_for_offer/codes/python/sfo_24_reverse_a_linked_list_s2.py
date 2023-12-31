"""
File: sfo_24_reverse_a_linked_list_s2.py
Created Time: 2021-12-09
Author: Krahets (krahets@163.com)
"""

from include import *


# ===== Solution Code =====
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        cur, pre = head, None
        while cur:
            cur.next, pre, cur = pre, cur, cur.next
        return pre


# ======= Test Case =======
head = list_to_linked_list([1, 2, 3, 4, 5])
# ====== Driver Code ======
slt = Solution()
res = slt.reverseList(head)
print_linked_list(res)
