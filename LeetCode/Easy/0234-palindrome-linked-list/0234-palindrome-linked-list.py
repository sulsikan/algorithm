# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # 런너를 이용한 풀이
        # fast, slow 두개로 풀이한다
        rev = None
        slow = fast = head
        while fast and fast.next:
            fast = fast.next.next
            rev, rev.next, slow = slow, rev, slow.next
        # 홀수 길이라면 한칸 더 이동
        if fast:
            slow = slow.next
        # 역순이랑 같은지 확인
        while rev and rev.val == slow.val:
            slow, rev = slow.next, rev.next
        # 끝까지 이동하면 None이니까 true를 반환함
        return not rev