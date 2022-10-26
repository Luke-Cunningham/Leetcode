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


#######################################################################################################################

class Solution20(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        dict = {"]": "[", "}": "{", ")": "("}
        for char in s:
            if char in dict.values():
                stack.append(char)
            elif char in dict.keys():
                if stack == [] or dict[char] != stack.pop():
                    return False
            else:
                return False
        return stack == []


class Solution13(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        roman_nums = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000

        }
        s_length = len(s)

        if s_length == 1:
            return roman_nums.get(s[0])
        sum = 0
        for i in range(s_length - 1):
            if roman_nums.get(s[i]) < roman_nums.get(s[i + 1]):
                sum -= roman_nums.get(s[i])
            else:
                sum += roman_nums.get(s[i])
        sum += roman_nums.get(s[-1])
        return sum


#######################################################################################################################

class Solution3(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        start = max_length = 0
        used = {}

        for i, char in enumerate(s):
            if char in used and start <= used[char]:
                start = used[char] + 1
            else:
                max_length = max(max_length, i - start + 1)
            used[char] = i

        return max_length


#######################################################################################################################

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution21(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        new_list = dummy = ListNode()

        while list1 and list2:
            if list1.val <= list2.val:
                new_list.next = list1
                list1, new_list = list1.next, list1

            else:
                new_list.next = list2
                list2, new_list = list2.next, list2

        if list1 or list2:
            new_list.next = list1 if list1 else list2

        return dummy.next


if __name__ == '__main__':
    s = Solution3()
    print(s.lengthOfLongestSubstring("abbbbdvdf"))
