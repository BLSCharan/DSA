def solve(head):
  
    if not head or not head.next or not head.next.next:
        return 0
 
    count = 0
    prev = head
    cur = head.next
    nxt = cur.next

    while nxt:
        if (cur.val < prev.val and cur.val < nxt.val) or (cur.val > prev.val and cur.val > nxt.val):
            count += 1
        prev = cur
        cur = nxt
        nxt = nxt.next

    return count
