class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hashmap = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in hashmap:
                return [i, hashmap[complement]]
            hashmap[num] = i


#######################################################################################################################
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution2(object):
    def addTwoNumbers(self, l1, l2):
        return_head = ListNode(0)
        curr = return_head
        carry = 0

        while l1 is not None or l2 is not None or carry != 0:
            l1val = l1.val if l1 else 0
            l2val = l2.val if l2 else 0

            c_sum = l1val + l2val + carry
            carry = c_sum // 10
            new_node = ListNode(c_sum % 10)
            curr.next = new_node
            curr = new_node

            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return return_head.next

    def lst2link(self, lst):
        cur = dummy = ListNode(0)
        for e in lst:
            cur.next = ListNode(e)
            cur = cur.next
        return dummy.next


if __name__ == '__main__':
    s = Solution()
    s.twoSum([3, 2, 4], 6)

    s2 = Solution2()
    list1 = [7, 4, 8]
    list2 = [4, 9, 6]
    llist1 = s2.lst2link(list1)
    llist2 = s2.lst2link(list2)
    s2.addTwoNumbers(llist1, llist2)
