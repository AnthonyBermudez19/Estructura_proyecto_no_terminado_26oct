def binary_search(tickets, target_id):
    left, right = 0, len(tickets) - 1
    while left <= right:
        mid = (left + right) // 2
        if tickets[mid].id == target_id:
            return tickets[mid]
        elif tickets[mid].id < target_id:
            left = mid + 1
        else:
            right = mid - 1
    return None
