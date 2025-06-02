class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        ptr = head
        seen = set()
        while ptr:
            if ptr not in seen:
                seen.add(ptr)
            else:
                return True
            ptr = ptr.next
        return False
        