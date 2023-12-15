

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        #first_node will be returned and cur will be used for processing
        first_node = cur = ListNode(0)
        
        carry = 0
        value = 0

        while l1 or l2 or carry:
            value = carry
            if l1:
                value += l1.val
                l1 = l1.next
            if l2:
                value += l2.val
                l2 = l2.next
            carry = value // 10

            cur.next = ListNode(value % 10)
            cur = cur.next
        # we are sending next as we initialized with 0 value
        return first_node.next


if __name__ == '__main__':
    a, a.next, a.next.next = ListNode(2), ListNode(4), ListNode(3)
    b, b.next, b.next.next = ListNode(5), ListNode(6), ListNode(4)
    result = Solution().addTwoNumbers(a, b)
    test = "{0} -> {1} -> {2}".format(result.val,
                                      result.next.val, result.next.next.val)
    print(test)
